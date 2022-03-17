from lib2to3.pytree import Base
import time
from brownie.network.account import LocalAccount
import requests
import sys
import math
from brownie import *
from brownie import Wei, network, Contract
from brownie.convert import EthAddress
from brownie.network.gas.strategies import LinearScalingStrategy
from brownie.network.state import Chain
from brownie.network import contract, gas_price, transaction, gas_limit
from web3.eth import Eth
from scripts.contract_abi import *
from scripts.user_config import *
from scripts.pancake_utils import getSwapQuote, getSwapPrices
from scripts.contract_storage import *
from inputimeout import inputimeout, TimeoutOccurred

if network.show_active() != "bsc-main":
    print("changing network to bsc-main")
    network.disconnect()
    network.connect("bsc-main")

"""-----------------------SYRUP POOL-----------------------"""


class ContractTool:
    def __init__(self, syrup_pool_address) -> None:
        self.pancake = Contract.from_abi(
            "Pancake", "0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82", ZAPPER_EXCHANGE
        )
        self.syrupPool = Contract.from_abi("Syrup Pool", syrup_pool_address, SYRUP_POOL)
        self.poolToken = Contract.from_abi(
            "Pool Token", self.syrupPool.rewardToken(), POOL_TOKEN
        )


spender_limit = Wei(
    115792089237316195423570985008687907853269984665640564039457584007913129639935
)


def approve(
    account,
    _spender_address,
    _spender_limit=spender_limit,
    _phase="approve only",
    confs: int = 0,
):
    if pancake_contract.allowance(account, _spender_address):
        print(f"{account}-- already approved")
        return TransactionObj(account, 0, 1, _phase)
    try:
        tx = pancake_contract.approve(
            _spender_address,
            _spender_limit,
            {"from": account, "required_confs": confs, "allow_revert": True},
        )
    except BaseException as err:
        print(err)
        return TransactionObj(account, 0, -1, _phase)
    return TransactionObj(account, tx.txid, tx.status, _phase)


def deposit(
    account: LocalAccount,
    _pool_contract,
    _amount="MAX",
    isIFO: bool = False,
    pid: int = 0,
    confs: int = 0,
):
    balance = pancake_contract.balanceOf(EthAddress(account))
    if balance <= 0:
        print(f"account {account}: insufficient balance...")
        return None
    if _amount == "MAX" or _amount > balance:
        _amount = balance

    if isIFO:
        pool_limit = _pool_contract.viewPoolInformation(pid)[2]
        user_credit = ifo_pool_contract.getUserCredit(
            EthAddress(account)
        ) - _pool_contract.userCreditUsed(account.address)
        pool_limit = pool_limit if pool_limit else balance
        _amount = min(_amount, pool_limit, user_credit)
    else:
        if _pool_contract.hasUserLimit():
            userLimit = (
                _pool_contract.poolLimitPerUser()
                - _pool_contract.userInfo(account.address)[0]
            )
            _amount = min(_amount, userLimit)
    _amount = Wei(_amount)
    if _amount <= 0:
        print(f"account {account}: insufficient balance...")
        return None
    print(f"{account}-- stake amount: {Wei(_amount).to('ether')} Pancake")
    if isIFO:
        try:
            tx = _pool_contract.depositPool(
                _amount,
                pid,
                {"from": account, "required_confs": confs, "allow_revert": True},
            )
        except BaseException as err:
            print(err)
            return TransactionObj(account, 0, -1, "deposit")
    else:
        try:
            tx = _pool_contract.deposit(
                _amount,
                {"from": account, "required_confs": confs, "allow_revert": True},
            )
        except BaseException as err:
            print(err)
            return TransactionObj(account, 0, -1, "deposit")
    return TransactionObj(account, tx.txid, tx.status, "deposit")


def withdraw(
    account,
    _pool_contract,
    _amount="MAX",
    isIFO: bool = False,
    pid: int = 0,
    phase="withdraw",
    confs: int = 0,
):
    if isIFO:
        """if _pool_contract.userInfo(account)[0] == 0:
        print(f"account {EthAddress(account)} nothing to withdraw")
        return None"""
        if _pool_contract == ifo_pool_contract:
            try:
                tx = _pool_contract.withdrawAll(
                    {"from": account, "required_confs": confs, "allow_revert": True}
                )
            except BaseException as err:
                print(err)
                return TransactionObj(account, 0, -1, "withdraw")
        else:
            try:
                tx = _pool_contract.harvestPool(
                    pid,
                    {"from": account, "required_confs": confs, "allow_revert": True},
                )
            except BaseException as err:
                print(err)
                return TransactionObj(account, 0, -1, "withdraw")
        return TransactionObj(account, tx.txid, tx.status, "withdraw")
    balance = _pool_contract.userInfo(EthAddress(account))[0]
    if balance <= 0:
        print(f"account {account}: insufficient balance...")
        return None
    if _amount == "MAX":
        _amount = balance
    _amount = Wei(_amount)
    print(f"{account}-- withdraw amount: {Wei(_amount).to('ether')} Pancake")
    if phase == "emergency withdraw":
        tx = _pool_contract.emergencyWithdraw(
            {"from": account, "required_confs": confs, "allow_revert": True}
        )
        return TransactionObj(account, tx.txid, tx.status, "emergency withdraw")
    try:
        tx = _pool_contract.withdraw(
            _amount, {"from": account, "required_confs": confs, "allow_revert": True}
        )
    except BaseException as err:
        print(err)
        return TransactionObj(account, 0, -1, "withdraw")
    return TransactionObj(account, tx.txid, tx.status, "withdraw")


def transfer(
    from_account,
    to_account,
    _token_contract,
    _amount="MAX",
    confs=0,
    offset=0,
):
    if from_account == to_account:
        print("cannot transfer to yourself...")
        return None
    balance = _token_contract.balanceOf(EthAddress(from_account))
    if balance <= 0:
        print(f"account {from_account}: insufficient balance...")
        return None
    if _amount == "MAX":
        _amount = balance
    if offset:
        _amount = offset - _token_contract.balanceOf(EthAddress(to_account))
        if _amount >= balance:
            print("insufficient amount...")
            return None
        if balance - _amount < offset:
            _amount = balance - offset
    if _amount < 0:
        print("<0 dont transfer")
        return None
    print(
        f"from: {from_account}-- to: {to_account}-- transfer amount: {Wei(_amount).to('ether')}"
    )
    try:
        tx = _token_contract.transfer(
            to_account,
            _amount,
            {"from": from_account, "required_confs": confs, "allow_revert": True},
        )
    except BaseException as err:
        print(err)
        return TransactionObj(from_account, 0, -1, "transfer")
    return TransactionObj(from_account, tx.txid, tx.status, "transfer")


def high_concurrency_transact(
    interactContract: Contract,
    _spender_limit=spender_limit,
    _phase: str = "approve only",
    _amount="MAX",
    accounts_list: list = accounts_list,
    to_account="0",
    isIFO: bool = False,
    pid: int = 0,
    confs: int = 0,
):
    transactionArr = []
    start_counter = time.time()
    chain = Chain()
    for account in accounts_list:
        print(f"account {accounts_list.index(account)+1}    {_phase}")
        if _phase in ["approve", "approve only"]:
            obj = approve(account, interactContract.address, _spender_limit, _phase)
        elif _phase == "deposit":
            obj = deposit(
                account,
                _amount=_amount,
                _pool_contract=interactContract,
                isIFO=isIFO,
                pid=pid,
            )
        elif _phase == "withdraw":
            obj = withdraw(
                account,
                _amount=_amount,
                _pool_contract=interactContract,
                isIFO=isIFO,
                pid=pid,
                phase=_phase,
            )
        elif _phase == "transfer":
            obj = transfer(
                account,
                to_account,
                _amount=_amount,
                _token_contract=interactContract,
                confs=confs,
            )
        elif _phase == "emergency withdraw":
            obj = withdraw(
                account,
                _amount=_amount,
                _pool_contract=interactContract,
                isIFO=isIFO,
                pid=pid,
                phase=_phase,
            )
        else:
            continue
        if obj:
            transactionArr.append(obj)

    finishCounter = 0
    gas_fee = 0
    while finishCounter < len(transactionArr):
        time.sleep(1)
        print(f"iterating {len(transactionArr)-finishCounter} transactions")
        for transact in transactionArr:
            if transact.get_phase() in ["finished", "dropped"]:
                continue
            presentTX = chain.get_transaction(transact.get_txid())
            status = presentTX.status
            if status == -1:  # pending
                transact.set_status(status)
                continue

            elif status == 0:  # reverted
                transact.set_status(status)
                print(
                    f"account: {transact.get_account()}  hash: {transact.get_txid()} reverted, instantiate a new transaction"
                )
                if _phase in ["approve", "approve only"]:
                    replaceObj = approve(
                        transact.get_account(), interactContract.address, _spender_limit
                    )
                elif _phase == "deposit":
                    replaceObj = deposit(
                        transact.get_account(),
                        _amount=_amount,
                        _pool_contract=interactContract,
                        isIFO=isIFO,
                        pid=pid,
                    )
                elif _phase == "withdraw":
                    replaceObj = withdraw(
                        transact.get_account(),
                        _amount=_amount,
                        _pool_contract=interactContract,
                        isIFO=isIFO,
                        pid=pid,
                        phase=_phase,
                    )
                elif _phase == "emergency withdraw":
                    replaceObj = withdraw(
                        transact.get_account(),
                        _amount=_amount,
                        _pool_contract=interactContract,
                        isIFO=isIFO,
                        pid=pid,
                        phase=_phase,
                    )
                elif _phase == "transfer":
                    replaceObj = transfer(
                        transact.get_account(),
                        to_account,
                        _amount=_amount,
                        _token_contract=interactContract,
                    )
                if not replaceObj:
                    print("abort transact...")
                    transact.set_phase("dropped")
                    finishCounter += 1
                    continue
                transact.set_txid(replaceObj.get_txid())
                transact.set_status(replaceObj.get_status())

            elif status == 1:  # confirmed
                transact.set_status(status)
                if transact.get_phase() in [
                    "withdraw",
                    "emergency withdraw",
                    "deposit",
                    "transfer",
                    "approve only",
                ]:
                    transact.set_phase("finished")
                    finishCounter += 1
                    print(
                        f"account: {transact.get_account()} phase: {transact.get_phase()} tx hash: {transact.get_txid()} confirmed"
                    )
                    gas_fee += presentTX.gas_price * presentTX.gas_used
                elif transact.get_phase() == "approve":
                    depositObj = deposit(
                        transact.get_account(),
                        _amount=_amount,
                        _pool_contract=interactContract,
                        isIFO=isIFO,
                        pid=pid,
                    )
                    if not depositObj:
                        print("abort transact...")
                        transact.set_phase("dropped")
                        finishCounter += 1
                        continue
                    transact.set_txid(depositObj.get_txid())
                    transact.set_status(depositObj.get_status())
                    transact.set_phase(depositObj.get_phase())
                    print(
                        f"account: {transact.get_account()} phase: {transact.get_phase()} tx hash: {transact.get_txid()} approved\nset phase to deposit"
                    )

            elif status == -2:  # dropped
                transact.set_status(status)
                transact.set_phase("dropped")
                finishCounter += 1
                print(
                    f"{transact.get_account()} has a dropped transaction, please check it manually."
                )
    end_counter = time.time()
    print(
        f"time counter: {end_counter - start_counter}     gas fee: {Wei(gas_fee).to('ether')} BNB"
    )
    return gas_fee


def wait_till_block(height: int):
    try:
        chain = Chain()
        currentHeight = chain.height
    except BaseException as err:
        print(err)
        return wait_till_block(height)

    while currentHeight < height:
        sys.stdout.write(
            f"current block: {currentHeight}...    starting block: {height}\r"
        )
        time.sleep(60)
        currentHeight = chain.height
        sys.stdout.flush()
    print(f"\nreached block {height}")


def latest_CHEF(CHEF_address: str = "0xFfF5812C35eC100dF51D5C9842e8cC3fe60f9ad7"):
    currentHeight = Chain().height
    startblock = currentHeight - 200000
    apiKey = bscScanKey
    url = (
        "https://api.bscscan.com/api?module=account&action=txlistinternal&address="
        + CHEF_address
        + "&startblock="
        + str(startblock)
        + "&endblock="
        + str(currentHeight)
        + "&page=1&offset=10&sort=asc&apikey="
        + apiKey
    )
    r = requests.get(url)
    print(r.json()["result"])
    latest_pool_address = r.json()["result"].pop()["contractAddress"]
    syrup_pool_contract = Contract.from_abi(
        "Latest Syrup Pool", latest_pool_address, SYRUP_POOL
    )
    pool_token_contract = Contract.from_abi(
        "Latest Pool Token", syrup_pool_contract.rewardToken(), POOL_TOKEN
    )
    print(
        f"Latest Syrup Pool: {pool_token_contract.symbol()}  address: {latest_pool_address}   token address: {syrup_pool_contract.rewardToken()}"
    )
    syrup_pool_contract.set_alias(pool_token_contract.symbol() + "_SYRUP")

    return syrup_pool_contract


def realTimeSwap(sellToken: Contract, account):
    USDT = "0x55d398326f99059fF775485246999027B3197955"
    while True:
        quote = getSwapQuote(
            sellToken.address, USDT, sellToken.balanceOf(account), account
        )
        price = quote["price"]
        guaranteedPrice = quote["guaranteedPrice"]

        print(f"price: {price}  guaranteedPrice: {guaranteedPrice}")
        try:
            exchange_permit = inputimeout("Enter Y to Exchange (y/n): ", 3)
            break
        except TimeoutOccurred:
            pass

    if exchange_permit in ["y", "Y"]:
        print("proceed")
        try:
            pancakeSwapExactTokensForTokens(account, sellToken)
        except BaseException as err:
            print(err)
    else:
        print(exchange_permit)
        print("abort transaction")


def hit_to_proceed():
    input("hit Enter to Proceed:")


def pancakeSwapExactTokensForTokens(
    account: LocalAccount,
    sellToken: Contract,
    buyToken: Contract = BSC_USDT_contract,
    sellAmount: int | str = "MAX",
    proceed: bool = False,
):
    # if possible, check if contract are BEP-20 token contract first
    if sellAmount == "MAX":
        sellAmount = sellToken.balanceOf(account)
    # check for approval
    if sellToken.allowance(account.address, pancake_router_v2.address) < sellAmount:
        print(
            f"insufficient allowance, aproving PancakeSwap to spend {sellToken.symbol()}"
        )
        sellToken.approve(pancake_router_v2.address, spender_limit, {"from": account})
    quote = getSwapQuote(
        sellToken.address,
        buyToken.address,
        sellAmount,
        account,
    )
    # check proportion of this swap, only proceed if PancakeSwap_V2 is 1, otherwise, exit this function, alert user to swap manually
    for source in quote["sources"]:
        if source["name"] == "PancakeSwap_V2":
            if source["proportion"] == "1":
                proceed = True
                break
    if proceed == False:
        print(quote)
        proceed = input(
            "the 0x suggestion of this swap is not entirely routed on PancakeSwap, if hit ENTER, we will still swap entirely on PancakeSwap: (or input N/n to stop)"
        )
        if proceed in ["N", "n"]:
            print("Aborted Swap...")
            return None

    chain = Chain()
    print(
        f"{account.address} \nsell: {Wei(quote['sellAmount']).to('ether')} {sellToken.symbol()} \nguaranteedPrice: {quote['guaranteedPrice']}"
    )
    try:
        tx = pancake_router_v2.swapExactTokensForTokens(
            int(quote["sellAmount"]),
            int(float(quote["sellAmount"]) * float(quote["guaranteedPrice"])),
            quote["orders"][0]["fillData"]["tokenAddressPath"],
            EthAddress(account),
            chain.time() + 300,
            {"from": account},
        )
    except BaseException:
        return pancakeSwapExactTokensForTokens(
            account, sellToken, buyToken, sellAmount, proceed
        )
    return TransactionObj(account, tx.txid, tx.status, "swap")


def main():
    pass
