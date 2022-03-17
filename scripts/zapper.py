from brownie.convert.datatypes import EthAddress
from brownie.network.account import Account
from brownie.network.main import gas_price
from brownie.network.state import Chain
from scripts.contract_abi import ZAPPER_EXCHANGE, AAVE_ZAP_IN, ZAPPER_LP
from scripts.user_config import accounts_KK, accounts_list, TransactionObj
from brownie import Contract, Wei
import requests
from brownie.network import gas_limit
import time
import sys
import json
from enum import IntEnum


class QuestID(IntEnum):
    LiquidityPool = 6
    Exchange = 7
    Save = 8


chain = Chain()
maxGas: int = 750000
gas_limit("auto")
exchange_contract = Contract.from_abi(
    "Exchange", "0xdef1c0ded9bec7f1a1670819833240f027b25eff", ZAPPER_EXCHANGE
)

save_contract = Contract.from_abi(
    "Save", "0x8DfDea6A4818d2AA7463edB9A8841cB0c04255aF", AAVE_ZAP_IN
)

lp_contract = Contract.from_abi(
    "Liquidity Pool", "0xF231be40d73a9E73d859955344A4fF74f448dF34", ZAPPER_LP
)


def decodeInput(data: str, contract: Contract):
    input_data = contract.decode_input(data)
    return input_data[1]


def getExchangeTransaction(
    ownerAddress,
    sell_token_address="0x0000000000000000000000000000000000000000",
    buy_token_address="0x2791bca1f2de4661ed88a30c99a7a9449aa84174",
    sellAmount=Wei("0.01 ether"),
    gasPrice=Wei("30 gwei"),
    slippage=0.03,
    api_key="5d1237c2-3840-4733-8e92-c5a58fe81b88",
):
    url = (
        "https://api.zapper.fi/v1/exchange/quote?api_key="
        + api_key
        + "&ownerAddress="
        + ownerAddress
        + "&sellTokenAddress="
        + sell_token_address
        + "&buyTokenAddress="
        + buy_token_address
        + "&sellAmount="
        + str(sellAmount)
        + "&gasPrice="
        + str(gasPrice)
        + "&gasBuffer=0.1&slippagePercentage="
        + str(slippage)
        + "&isZap=false&network=polygon"
    )
    r = requests.get(url)
    return r.json()


def getSaveTransaction(
    owner_address,
    api_key="5d1237c2-3840-4733-8e92-c5a58fe81b88",
    pool_address="0x1a13f4ca1d028320a707d99520abfefca3998b7f",
    sell_token_address="0x0000000000000000000000000000000000000000",
    sellAmount=10000000000000000,
    gasPrice=Wei("30 gwei"),
    slippage=0.03,
):
    url = (
        "https://api.zapper.fi/v1/zap-in/interest-bearing/aave-v2/transaction?api_key="
        + api_key
        + "&ownerAddress="
        + owner_address
        + "&poolAddress="
        + pool_address
        + "&sellTokenAddress="
        + sell_token_address
        + "&sellAmount="
        + str(sellAmount)
        + "&gasPrice="
        + str(gasPrice)
        + "&slippagePercentage="
        + str(slippage)
        + "&network=polygon"
    )
    r = requests.get(url)
    return r.json()


def getLPTransaction(
    ownerAddress,
    api_key="5d1237c2-3840-4733-8e92-c5a58fe81b88",
    poolAddress="0x6e7a5fafcec6bb1e78bae2a1f0b612012bf14827",
    sellTokenAddress="0x0000000000000000000000000000000000000000",
    sellAmount=Wei("0.2 ether"),
    gasPrice=Wei("30 gwei"),
    slippage=0.03,
):
    url = (
        "https://api.zapper.fi/v1/zap-in/pool/quickswap/transaction?api_key="
        + api_key
        + "&ownerAddress="
        + ownerAddress
        + "&poolAddress="
        + poolAddress
        + "&sellTokenAddress="
        + sellTokenAddress
        + "&sellAmount="
        + str(sellAmount)
        + "&gasPrice="
        + str(gasPrice)
        + "&slippagePercentage="
        + str(slippage)
        + "&network=polygon"
    )
    r = requests.get(url)
    return r.json()


def zapper_exchange(
    ownerAddress,
    sell_token_address="0x0000000000000000000000000000000000000000",
    buy_token_address="0x2791bca1f2de4661ed88a30c99a7a9449aa84174",
    sellAmount=Wei("0.01 ether"),
    gasPrice=Wei("30 gwei"),
    slippage=0.03,
    api_key="5d1237c2-3840-4733-8e92-c5a58fe81b88",
    confs=0,
):
    r = getExchangeTransaction(
        EthAddress(ownerAddress),
        sell_token_address,
        buy_token_address,
        sellAmount,
        gasPrice,
        slippage,
        api_key,
    )
    if "statusCode" in r.keys():
        print(r)
        return None

    transactInput = decodeInput(r["data"], exchange_contract)
    estimated_max_gas = int(r["gas"])
    if estimated_max_gas > maxGas:
        print(
            f"estimated gas: {estimated_max_gas} too high, if you choose to process, please set gas limit manually."
        )
        return None
    print(
        f"address: {EthAddress(ownerAddress)}    phase: exchange    amount: {sellAmount}"
    )
    try:
        tx = exchange_contract.transformERC20(
            transactInput[0],
            transactInput[1],
            transactInput[2],
            transactInput[3],
            transactInput[4],
            {
                "from": ownerAddress,
                "value": transactInput[2],
                "gas_price": Wei(int(r["gasPrice"])),
                "allow_revert": True,
                "required_confs": confs,
            },
        )
    except ValueError:
        print(ValueError)
        tx = TransactionObj(ownerAddress, 0, 0, "exchange")
    return TransactionObj(ownerAddress, tx.txid, tx.status, "exchange")


def zapper_save(
    ownerAddress,
    api_key="5d1237c2-3840-4733-8e92-c5a58fe81b88",
    pool_address="0x1a13f4ca1d028320a707d99520abfefca3998b7f",
    sell_token_address="0x0000000000000000000000000000000000000000",
    sellAmount=10000000000000000,
    gasPrice=Wei("30 gwei"),
    slippage=0.03,
    confs=0,
):
    r = getSaveTransaction(
        EthAddress(ownerAddress),
        api_key,
        pool_address,
        sell_token_address,
        sellAmount,
        gasPrice,
        slippage,
    )
    if "statusCode" in r.keys():
        print(r)
        return None

    transactInput = decodeInput(r["data"], save_contract)
    estimated_max_gas = int(r["gas"])
    if estimated_max_gas > maxGas:
        print(
            f"estimated gas: {estimated_max_gas} too high, if you choose to process, please set gas limit manually."
        )
        return None
    print(f"address: {EthAddress(ownerAddress)}    phase: save    amount: {sellAmount}")
    try:
        tx = save_contract.ZapIn(
            transactInput[0],
            transactInput[1],
            transactInput[2],
            transactInput[3],
            transactInput[4],
            transactInput[5],
            transactInput[6],
            {
                "from": ownerAddress,
                "value": transactInput[1],
                "gas_price": Wei(int(r["gasPrice"])),
                "allow_revert": True,
                "required_confs": confs,
            },
        )
    except ValueError:
        print(ValueError)
        tx = TransactionObj(ownerAddress, 0, 0, "save")
    return TransactionObj(ownerAddress, tx.txid, tx.status, "save")


def zapper_lp(
    ownerAddress,
    api_key="5d1237c2-3840-4733-8e92-c5a58fe81b88",
    poolAddress="0x6e7a5fafcec6bb1e78bae2a1f0b612012bf14827",
    sellTokenAddress="0x0000000000000000000000000000000000000000",
    sellAmount=Wei("0.1 ether"),
    gasPrice=Wei("30 gwei"),
    slippage=0.03,
    confs=0,
):
    r = getLPTransaction(
        EthAddress(ownerAddress),
        api_key,
        poolAddress,
        sellTokenAddress,
        sellAmount,
        gasPrice,
        slippage,
    )
    if "statusCode" in r.keys():
        print(r)
        return None

    transactInput = decodeInput(r["data"], lp_contract)
    estimated_max_gas = int(r["gas"])
    if estimated_max_gas > maxGas:
        print(
            f"estimated gas: {estimated_max_gas} too high, if you choose to process, please set gas limit manually."
        )
        return None
    print(
        f"address: {EthAddress(ownerAddress)}    phase: liquidity pool    amount: {sellAmount}"
    )
    try:
        tx = lp_contract.ZapIn(
            transactInput[0],
            transactInput[1],
            transactInput[2],
            transactInput[3],
            transactInput[4],
            transactInput[5],
            transactInput[6],
            transactInput[7],
            transactInput[8],
            {
                "from": ownerAddress,
                "value": transactInput[2],
                "gas_price": Wei(int(r["gasPrice"])),
                "allow_revert": True,
                "required_confs": confs,
            },
        )
    except ValueError:
        print(ValueError)
        tx = TransactionObj(ownerAddress, 0, 0, "liquidity pool")
    return TransactionObj(ownerAddress, tx.txid, tx.status, "liquidity pool")


def getQuest(ownerAddress, api_key="5d1237c2-3840-4733-8e92-c5a58fe81b88"):
    url = (
        "https://api.zapper.fi/v1/gamification/users/"
        + EthAddress(ownerAddress)
        + "/available-quests?api_key="
        + api_key
    )
    r = requests.get(url)
    if r.status_code != 200:
        return getQuest(ownerAddress, api_key)
    return r.json()


def get_todo_quests(
    _accounts_list: list,
    prop: str = "isCompletable",
    api_key="5d1237c2-3840-4733-8e92-c5a58fe81b88",
):
    daily_sign_list = []
    exchange_quest_list = []
    save_quest_list = []
    lp_quest_list = []
    print(
        f"Getting {len(_accounts_list)} account's quest detail, it should take few minutes..."
    )
    for account in _accounts_list:
        sys.stdout.write(
            f"getting account{_accounts_list.index(account)+1}: {EthAddress(account)} complitable quest (weekly)\r"
        )
        r = getQuest(account, api_key)
        del r[0]  # get rid off Open Zapper quest
        r.pop()  # get rid off Avatar quest
        for quest in r:
            if quest[prop]:
                id = quest["id"]
                account = EthAddress(account)
                if id == 5:
                    daily_sign_list.append(account)
                elif id == 6:
                    lp_quest_list.append(account)
                elif id == 7:
                    exchange_quest_list.append(account)
                elif id == 8:
                    save_quest_list.append(account)
        time.sleep(0.25)
        sys.stdout.flush()
    return {
        5: daily_sign_list,
        6: lp_quest_list,
        7: exchange_quest_list,
        8: save_quest_list,
    }


def high_concurrency_transact(
    _accounts_list,
    quest_id: QuestID | None = None,
    api_key="5d1237c2-3840-4733-8e92-c5a58fe81b88",
):
    start_counter = time.time()
    quests_dict = get_todo_quests(_accounts_list, api_key)
    transactionArr = []
    for account in quests_dict[quest_id]:
        if quest_id == 6:
            transactObject = zapper_lp(account, api_key=api_key)
        elif quest_id == 7:
            transactObject = zapper_exchange(account, api_key=api_key)
        elif quest_id == 8:
            transactObject = zapper_save(account, api_key=api_key)
        if transactObject:
            transactionArr.append(transactObject)
    finishCounter = 0
    while finishCounter < len(transactionArr):
        time.sleep(3)
        print(f"iterating {len(transactionArr)-finishCounter} transactions")
        for transact in transactionArr:
            phase = transact.get_phase()
            if phase in ["finished", "dropped"]:
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
                if phase == "liquidity pool":
                    replaceObj = zapper_lp(transact.get_account(), api_key=api_key)
                elif phase == "exchange":
                    replaceObj = zapper_exchange(
                        transact.get_account(), api_key=api_key
                    )
                elif phase == "save":
                    replaceObj = zapper_save(transact.get_account(), api_key=api_key)
                if not replaceObj:
                    print("abort transact...")
                    transact.set_phase("dropped")
                    finishCounter += 1
                    continue
                transact.set_txid(replaceObj.get_txid())
                transact.set_status(replaceObj.get_status())

            elif status == 1:  # confirmed
                transact.set_status(status)
                transact.set_phase("finished")
                finishCounter += 1
                print(
                    f"account: {transact.get_account()} phase: {transact.get_phase()} tx hash: {transact.get_txid()} confirmed"
                )

            elif status == -2:  # dropped
                transact.set_status(status)
                transact.set_phase("dropped")
                finishCounter += 1
                print(
                    f"{transact.get_account()} has a dropped transaction, please check it manually."
                )

    end_counter = time.time()
    print(f"time counter: {end_counter - start_counter}")


def questBy_Id(account, quest_id: int, confs=1):
    if quest_id == 6:
        obj = zapper_lp(account, confs=confs)
    elif quest_id == 7:
        obj = zapper_exchange(account, confs=confs)
    elif quest_id == 8:
        obj = zapper_save(account, confs=confs)
    if obj and obj.get_status() in [0, -2]:
        print("retransact...")
        questBy_Id(account, quest_id, confs)


def step_by_step(_accounts_list: list, quest_id: QuestID):
    start_counter = time.time()
    for account in _accounts_list:
        loop_counter = time.time()
        isCompletable = getQuest(account)[quest_id - 5]["isCompletable"]
        if isCompletable:
            # top_up_balance(account, accounts_list[0], Wei("0.6 ether"))
            questBy_Id(account, quest_id)
            print(
                f"account {_accounts_list.index(account) + 1} {EthAddress(account)}--  timer: {time.time()-loop_counter}\n\n"
            )
        else:
            print(
                f"account {_accounts_list.index(account) + 1} {EthAddress(account)}-- quest ID: {quest_id}-- already finished"
            )
    end_counter = time.time()
    print(f"whole time: {end_counter-start_counter}")


def top_up_balance(recipient: Account, sender: Account, balance_needed: Wei):
    if recipient == sender:
        print("cannot transfer to yourself...")
        return None
    if recipient.balance() < balance_needed:
        if sender.balance() - recipient.balance() < balance_needed:
            print(
                f"sender account: {EthAddress(sender)} doesn't have enough balance: {sender.balance()}"
            )
        top_up_amount = balance_needed - recipient.balance()
        print(f"sending amount: {top_up_amount} to account: {EthAddress(recipient)}")
        sender.transfer(recipient, top_up_amount, allow_revert=True)


def main():
    """quest_list = accounts_list[:20]

    step_by_step(quest_list, 7)"""
    # questBy_Id(accounts_KK[4], 7)

    """ quest_list_mappings: dict = {}
    for account in quest_list:
        quest_list_mappings[EthAddress(account)] = account """

    """ for account in accounts_list + accounts_KK:
        top_up_balance(account, accounts_list[0], Wei("0.2 ether")) """
    # step_by_step(accounts_list + accounts_KK, 6)
    # step_by_step(accounts_list + accounts_KK, 8)
    """ quests = get_todo_quests(accounts_list + accounts_KK, "isCompletable")
    with open("quests.json", "w") as f:
        json.dump(quests, f, indent=4) """
    with open("address_book.txt", "w") as f:
        for account in accounts_KK:
            addressDetail = (
                f"account {accounts_KK.index(account) + 1}: {EthAddress(account)}\n"
            )
            f.writelines(addressDetail)
