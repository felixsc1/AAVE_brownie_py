Tutorial code for using the DeFi Service AAVE with python.

# Goals:

1. Swap ETH for WETH
2. Deposit WETH on AAVE.
3. Borrow some asset with ETH collateral.
   a). Sell that borrowed asset (aka short selling)
4. Repay everything back

# Testing:

- Integration test: Kovan
- Unit tests: mainnet-fork (since no oracles are used)
