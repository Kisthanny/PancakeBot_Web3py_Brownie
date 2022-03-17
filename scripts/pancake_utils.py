from brownie.convert.datatypes import EthAddress, Wei
from brownie.network.account import Accounts, LocalAccount
import requests
from brownie import accounts, Wei


def getSwapQuote(sellToken: str, buyToken: str, sellAmount: Wei, account: LocalAccount):
    url = (
        "https://bsc.api.0x.org/swap/v1/quote?"
        + "buyToken="
        + buyToken
        + "&sellToken="
        + sellToken
        + "&sellAmount="
        + str(sellAmount)
        + "&takerAddress="
        + EthAddress(account)
        + "&skipValidation=true"
    )
    try:
        r = requests.get(url)
    except BaseException as err:
        print(err)
        return getSwapQuote(sellToken, buyToken, sellAmount, account)
    return r.json()


def getSwapPrices(sellToken: str):
    return requests.get(
        "https://bsc.api.0x.org/swap/v1/prices?sellToken=" + sellToken
    ).json()


def main():
    pass
