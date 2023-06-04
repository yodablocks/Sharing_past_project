# Chapter 6: Transfer assets on zkSync

Great job! Now that you've mastered deposits, it's time to learn how you can transfer assets on zkSync.

Basically, it's a two-step process:

1. You call the `syncTransfer` function of your zkSync wallet, specifying the recipient's address, the token you want to transfer, and the fee. Make sure you store the function's return value in a `const` variable as you'll use in the next step:

  ```JavaScript
  const transfer = await wallet.syncTransfer({
    to: toAddress,
    token: token,
    amount: closestPackableAmount,
    fee: closestPackableFee
  })
  ```

2. Calling the function above gets you halfway there. Next, you must monitor the status of your transfer:

  ```JavaScript
  const transferReceipt = await transfer.awaitReceipt()
  ```

At this point, you are almost ready to start fleshing out the function that transfers assets on zkSync.

Wait a little bit! Now there's one thing that deserves a special note. The precision of transfer operations on zkSync is limited, meaning that the transfer amounts should be packable to **5-byte long floating-point** representations, and fees paid should be packable to **2-byte long floating-point** representations.

Luckily zkSync provides two functions that hide the complexity of doing such computations:

```JavaScript
const closestPackableAmount = zksync.utils.closestPackableTransactionAmount(amountToTransferInWei)
const closestPackableFee = zksync.utils.closestPackableTransactionFee(transferFeeInWei)
```

## Put it to the test

We've gone ahead and declared the `transfer` function for you. Let's flesh it out.

1. Call the `closestPackableTransactionAmount` function, and store the result in a `const` variable named `closestPackableAmount`. Don't forget that you should convert the amount to `wei` by calling the `utils.parseEther` function. If you can't remember the syntax for doing this, see the previous chapter for details — but try to do it without peeking first to test your knowledge.

2. Call the `closestPackableFee` function, and store the result in a `const` variable named `closestPackableFee`. Don't forget to convert the amount to `wei` by calling the `utils.parseEther` function.

3. Once you have computed the amount to transfer and the fee, you should now call the async function `from.syncTransfer`, and store the result in a `const` variable named `transfer`.

4. Let's now call the `await transfer.awaitReceipt` function and store the result in a `const` named `transferReceipt`.

5. Lastly, copy and paste the following two lines of code:

  ```JavaScript
  console.log('Got transfer receipt.')
  console.log(transferReceipt)
  ```
