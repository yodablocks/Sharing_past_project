# Chapter 15: Putting everything together

We're close to being done here!

Now let's say Alice wants to withdraw her tokens to Ethereum. This is a two-step process:

1. Retrieve the withdrawal transfer fee
2. Withdraw assets from zkSync to Ethereum

If you didn't use the "**_Show me the answer_**" button to finish the previous lesson, the steps in this lesson should be a walk in the park.

## Put it to the test

1. Declare a `const` variable named `withdrawalFee`, and use it to store the value returned by a call to the `utils.getFee` function. The arguments for the `utils.getFee` call should be mostly the same as the previous time it was called to figure out the fee for a 'Transfer', just replace the first argument with `'Withdraw'`.

2. Call the `async` function `utils.withdrawToEthereum`. It takes the following parameters: `aliceZkSyncWallet`, `amountToWithdraw`, `withdrawalFee`, `token`, `zksync`, `ethers`.

# Give it a try!

That's it! Now you're ready to run your new apps. We trust you'll be able to do it.
