from scripts.user_config import accounts_KK, TransactionObj
from brownie import accounts
from brownie.network.state import Chain
import time


def transfer(from_account, to_account, amount):
    if to_account == from_account:
        print("can not transfer to yourself...")
        return None
    if from_account.balance() <= amount:
        print("insufficient balance...")
        return None
    print(f"transfer    from: {from_account}--  to: {to_account}--  amount: {amount}")
    tx = from_account.transfer(to_account, amount, required_confs=0)
    return TransactionObj(from_account, tx.txid, tx.status, "transfer")


def high_concurrency_transact(accounts_list, amount, _phase):
    transactionArr = []
    chain = Chain()
    for account in accounts_list:
        if _phase == "transfer":
            obj = transfer(accounts_list[0], account, amount)

        if obj:
            transactionArr.append(obj)

    finishCounter = 0
    while finishCounter < len(transactionArr):
        time.sleep(3)
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
                    f"account: {transact.get_account()} {transact.get_txid()} reverted, instantiate a new transaction"
                )
                if _phase == "transfer":
                    replaceObj = transfer(
                        accounts_list[0], transact.get_account(), amount
                    )
                transact.set_txid(replaceObj.get_txid())
                transact.set_status(replaceObj.get_status())
            elif status == 1:  # confirmed
                transact.set_status(status)
                if transact.get_phase() in [
                    "withdraw",
                    "deposit",
                    "transfer",
                    "approve only",
                ]:
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
                    f"{transact.get_account()} has a dropped transaction, please check it maually."
                )


def main():
    high_concurrency_transact(accounts_KK, "0.08 ether", "transfer")
