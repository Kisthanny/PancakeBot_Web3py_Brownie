from typing import Tuple
from brownie.convert.datatypes import EthAddress
from brownie.network import gas_price, gas_limit
from brownie.network.account import Account
from brownie.network.gas.strategies import GasNowStrategy, SimpleGasStrategy
from scripts.user_config import accounts_KK, accounts_list
from brownie import Wei, network, Contract
from scripts.contract_abi import ZAPPER_NFT
import sys, time, requests, json, math
from brownie.exceptions import (
    ContractNotFound,
    TransactionError,
    UnknownAccount,
    VirtualMachineError,
)


def showbalance(account_list: list):
    for account in account_list:
        if account.balance() < Wei("0.01 ether"):
            print(
                f"account {account_list.index(account) + 1}: {EthAddress(account)} balance: {account.balance().to('ether')}"
            )


class GasTracker:
    gasNow: float
    gasMin: float | None = None
    gasMax: float | None = None

    def __init__(self, timer: float | None = None) -> None:
        GasTracker.gasNow = self.gasTracker()
        if GasTracker.gasMin:
            GasTracker.gasMin = min(GasTracker.gasNow, GasTracker.gasMin)
        else:
            GasTracker.gasMin = GasTracker.gasNow
        if GasTracker.gasMax:
            GasTracker.gasMax = max(GasTracker.gasNow, GasTracker.gasMax)
        else:
            GasTracker.gasMax = GasTracker.gasNow
        if timer:
            self.timer = timer
        return None

    def gasTracker(self):
        try:
            r = requests.get(
                "https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=E7427E67VH1REU75KKIS7D552SI1C86FJS"
            )
        except BaseException:
            time.sleep(5)
            return self.gasTracker()
        if r.status_code != 200:
            return self.gasTracker()
        if r.json()["result"] == "Invalid API Key":
            print(
                "\nInvalid API Key, etherscan username: Kisthanny password should be: 5rWg23vPW/46Z&!"
            )
        return float(r.json()["result"]["suggestBaseFee"])

    def updateGas(self):
        GasTracker.gasNow = self.gasTracker()
        GasTracker.gasMin = min(GasTracker.gasNow, GasTracker.gasMin)
        GasTracker.gasMax = max(GasTracker.gasNow, GasTracker.gasMax)
        sys.stdout.write(
            f"  Now: {round(GasTracker.gasNow, 2)} gWei   Min: {round(GasTracker.gasMin, 2)} gWei   Max: {round(GasTracker.gasMax, 2)} gWei    "
        )
        if self.timer:
            sys.stdout.write(f"timer: {round(time.time()-self.timer, 2)}\r")
        sys.stdout.flush()
        return GasTracker.gasNow


def getPendingVolt(account):
    r = requests.get(
        "https://api.zapper.fi/v1/gamification/users/"
        + EthAddress(account)
        + "?api_key=96e0cc51-a62e-42ca-acee-910ea7d2a241"
    )
    if r.status_code != 200:
        return getPendingVolt(account)
    return r.json()["pendingZp"]


zapper_nft = Contract.from_abi(
    "zapper nft", "0xF1F3ca6268f330fDa08418db12171c3173eE39C9", ZAPPER_NFT
)


def claimVolts(account):
    pendingVolts = getPendingVolt(account)
    if pendingVolts < 9000:
        print(f"account {EthAddress(account)} pending: {pendingVolts}")
        return None
    while True:
        if GasTracker().gasNow <= 60.00:
            break
    with open("signatures.json", "r") as f:
        sig = json.load(f)[EthAddress(account)]
    try:
        zapper_nft.claimVolts(pendingVolts, sig, {"from": account})
    except TransactionError:
        time.sleep(30)
        claimVolts(account)


def mintNft(account: Account, id: int, gasTracker: GasTracker, baseGasFee: float):
    volts = zapper_nft.voltBalance(account)
    if volts < 9000:
        print(
            f"account {(accounts_list+accounts_KK).index(account)+1} less than 9000 volts"
        )
        return None
    quantity = volts // 9000

    while Wei(f"{gasTracker.updateGas()} gwei") * estimateGasCost(
        zapper_nft, "0x1b2ef1ca", id, quantity, {"from": account}
    ) > Wei(f"{baseGasFee} ether"):
        time.sleep(100000 / 60 / 60 / 24)
    # do the mint
    print(f"\naccount {(accounts_KK+accounts_list).index(account)+1} mint now...")
    zapper_nft.mint(id, quantity, {"from": account})


def estimateGasCost(contract: Contract, calldata: str, *args: Tuple):
    return contract.get_method_object(calldata).estimate_gas(*args)


def main():
    """for account in accounts_list[:10]:
    if account.balance() < Wei("0.005 ether"):
        print(
            f"account {(accounts_list+accounts_KK).index(account)+1} balance less than 0.005 ETH"
        )
        continue
    gasTracker = GasTracker(timer=time.time())
    mintNft(account, 19, gasTracker, 0.005)"""
    gasTracker = GasTracker(timer=time.time())
    while 1:
        gasTracker.updateGas()
        time.sleep(5)
