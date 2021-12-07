from brownie import config, network, interface
from scripts.helpful_scripts import get_account, FORKED_LOCAL_ENVIRONMENTS
from scripts.get_weth import get_weth


def main():
    account = get_account()
    erc20_address = config["networks"][network.show_active()]["weth_token"]
    if network.show_active() in FORKED_LOCAL_ENVIRONMENTS:
        get_weth(0.1)
    lending_pool = get_lending_pool()
    print(lending_pool)


def get_lending_pool():
    # as usual, we need ABI and address for contract.
    # ABI created from our interface, which we import from brownie and provide the address to it
    lending_pool_addresses_provider = interface.ILendingPoolAddressesProvider(
        config["networks"][network.show_active()]["lending_pool_addresses_provider"])
    lending_pool_address = lending_pool_addresses_provider.getLendingPool()
    lending_pool = interface.ILendingPool(lending_pool_address)
    return lending_pool
