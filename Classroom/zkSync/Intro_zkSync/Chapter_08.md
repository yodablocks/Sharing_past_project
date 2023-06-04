# Chapter 8: Withdraw to Ethereum

Awesome, you wrapped up the function that transfers assets on zkSync. This is no small feat, so pat yourself on the back. Now let's look at the logic for withdrawing assets.

I have good news for you - it consists of the same three basic steps!

1. You should start by computing the `closestPackableAmount` to withdraw.
2. Once you've retrieved the amount to withdraw, you can call the `wallet.withdrawFromSyncToEthereum` to withdraw your assets like so:
  ```JavaScript
  const withdraw = await wallet.withdrawFromSyncToEthereum({
    ethAddress: recipientEthereumAddress,
    token: token,
    amount: closestPackableAmount,
    fee: closestPackableFee
  })
  ```
3. Finally, monitor the status of your withdrawal by calling the `awaitVerifyReceipt` function.

You may have noticed that there are a few differences:
* This time, the first parameter you'll pass to the `wallet.withdrawFromSyncToEthereum` function is the recipient's **Ethereum** address.
* You'll use the `awaitVerifyReceipt` to monitor the status of your transaction

## Put it to the test

We've gone ahead and created an empty shell of the `withdrawToEthereum` function you'll be implementing in this lesson. Time to withdraw assets!

1. The first line of the function should call the `zksync.utils.closestPackableTransactionAmount`, and store the result in a `const` variable named `closestPackableAmount`. This function expects one parameter: the amount to withdraw. Use `ethers.utils.parseEther` to convert the amount to `wei`!

2. Similarly to the first step, call `zksync.utils.closestPackableTransactionFee` and store the fee in a `const` variable called `closestPackableFee`.

3. Declare a `const` variable called `withdraw` and assign it to the value of calling `await wallet.withdrawFromSyncToEthereum`. Use `wallet.address()` to determine the recipient's Ethereum address.

4. Invoke the `withdraw.awaitVerifyReceipt` function, and `await` for the promise to resolve.
