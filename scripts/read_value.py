from brownie import SimpleStorage, accounts, config


def read_contract():
    print(type(SimpleStorage[0]))


def main():
    read_contract()
