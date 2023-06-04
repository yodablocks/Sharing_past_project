# Chapter 3: Approve ERC20 token transfers

To transfer tokens on Ethereum, you must first allow the spender address to spend up to a certain amount of your tokens. This value is called the **allowance**, and the spender is only able to spend within the limits of the specified allowance.

Why is this important, you ask?

When you deposit tokens from Ethereum to zkSync, what happens under the hood is that your tokens are transferred to the zkSync smart contract running on the Ethereum network. So, before you actually deposit Alice's USDT tokens to zkSync, you'll have to approve the zkSync smart contract running on the Ethereum network to take her tokens.

For convenience, the `zksync.Wallet` object provides a function named `approveERC20TokenDeposits` that you only have to call once. It approves the zkSync smart contract to spend the maximum amount of ERC20 tokens, and you won't have to set the allowance for each deposit.

For a more granular control over your tokens, you can also approve each deposit, but you'll have to write the code yourself. The zksync JavaScript library doesn't provide a function for this.

## Put it to the test.


1. Call the `aliceZkSyncWallet.approveERC20TokenDeposits`, passing it `token` as an argument. It's an async function, so don't forget to prepend the `await` keyword!
