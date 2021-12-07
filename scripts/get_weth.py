from scripts.helpful_scripts import get_account
from brownie import interface, config, network


def main():
    get_weth(0.1)


def get_weth(_amountETH):
    account = get_account()
    weth = interface.IWeth(
        config["networks"][network.show_active()]["weth_token"])
    tx = weth.deposit({"from": account, "value": _amountETH * 10 ** 18})
    print("Received 0.1 WETH")
    return tx
