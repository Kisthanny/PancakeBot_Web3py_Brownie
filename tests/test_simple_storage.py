from brownie import SimpleStorage, accounts


def test_deploy():
    # Arrage
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    # Assert
    assert starting_value == expected


def test_updating_storage():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)  # wait(1) to avoid a brownie bug
    expected = 15
    assert expected == simple_storage.retrieve()
