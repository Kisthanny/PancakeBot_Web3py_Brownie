from brownie import accounts, config, SimpleStorage, network, Wei
from brownie.network.state import Chain

from brownie.convert.datatypes import EthAddress
from scripts.user_config import accounts_rinkeby


def deploy_simple_storage():
    account = get_account()
    return SimpleStorage.deploy({"from": account})


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts_rinkeby[0]


class TransactionObj:
    def __init__(self, account, txid, status, phase) -> None:
        self.account = account
        self.txid = txid
        self.status = status
        self.phase = phase

    def get_account(self):
        return self.account

    def get_txid(self):
        return self.txid

    def get_status(self):
        return self.status

    def get_phase(self):
        return self.phase

    def set_account(self, _account):
        self.account = _account

    def set_txid(self, _txid):
        self.account = _txid

    def set_status(self, _status):
        self.account = _status

    def set_phase(self, _phase):
        self.account = _phase


# tx = chain.get_transaction("0xD841C3B138B115A5F31E7C0C7EAE44DC2528E51EA40C4F0149FF1DDF9D95DD3F")
def test_silent():
    transactionArr = []
    simple_storage = SimpleStorage[-1]
    chain = Chain()
    for i in range(10):
        tx = simple_storage.addPerson(
            "test" + str(i),
            i,
            {"from": accounts_rinkeby[i], "required_confs": 0},
        )
        transactionArr.append(
            TransactionObj(accounts_rinkeby[i], tx.txid, tx.status, "addPerson")
        )

    finishCounter = 0
    while finishCounter < len(transactionArr):
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
                print(f"{transact.get_txid()} reverted, instantiate a new transaction")

                tx = simple_storage.addPerson(
                    "test" + str(i) + str(finishCounter),
                    finishCounter,
                    {"from": transact.get_account(), "required_confs": 0},
                )

                transact.set_txid(tx.txid)
                transact.set_status(tx.status)

            elif status == 1:  # confirmed
                transact.set_status(status)
                if transact.get_phase() == "addPerson":
                    transact.set_phase("finished")
                    finishCounter += 1
                    print(
                        f"account: {transact.get_account()} tx hash: {transact.get_txid()} confirmed"
                    )
            elif status == -2:  # dropped
                transact.set_status(status)
                transact.set_phase("dropped")
                finishCounter += 1
                print(
                    f"{transact.get_account()} has a dropped transaction, please check it maually."
                )


def main():
    account = get_account()
    simple_contract = deploy_simple_storage()
    tx = simple_contract.store(2, {"from": account})
    tx.wait(1)
    tx.gas
