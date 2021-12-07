from brownie import config, network, interface
from scripts.helpful_scripts import get_account, FORKED_LOCAL_ENVIRONMENTS
from scripts.get_weth import get_weth
from web3 import Web3

# amount to allow during verify step:
amount = Web3.toWei(0.1, "ether")


def main():
    account = get_account()
    erc20_address = config["networks"][network.show_active()]["weth_token"]
    if network.show_active() in FORKED_LOCAL_ENVIRONMENTS:
        get_weth(0.1)
    lending_pool = get_lending_pool()
    approve_erc20(amount, lending_pool.address, erc20_address, account)


def approve_erc20(amount, spender, erc20_address, account):
    print("Approving ERC20 token...")
    erc20 = interface.IERC20(erc20_address)
    tx = erc20.approve(spender, amount, {"from": account})
    tx.wait(1)
    print("Approved!")
    return tx


def get_lending_pool():
    # as usual, we need ABI and address for contract.
    # ABI created from our interface, which we import from brownie and provide the address to it
    lending_pool_addresses_provider = interface.ILendingPoolAddressesProvider(
        config["networks"][network.show_active()]["lending_pool_addresses_provider"])
    lending_pool_address = lending_pool_addresses_provider.getLendingPool()
    lending_pool = interface.ILendingPool(lending_pool_address)
    return lending_pool
