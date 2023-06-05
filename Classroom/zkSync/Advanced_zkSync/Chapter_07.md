# Chapter 7: Update the transfer function

Now that you've wrapped up the `displayZkSyncBalance` function, let's move forward to the `transfer` function.

Here's what you'll do in this chapter:

* Modify the `transfer` function declaration to take a `TokenSet` instance as the last parameter.
* Use the `tokenSet.parseToken` function to convert the `amountToTransfer` and `fee` variables from a human-readable form to `BigNumber`.

> 👉🏻 If you can't remember how to use the `tokenSet.parseToken` function, here's a quick refresher:


  ```JavaScript
  const amountAsBigNumber = tokenSet.parseToken(token, amountInHumanReadableForm)
  ```

  This simple example converts `amountInHumanReadableForm` tokens to `BigNumber` and stores the result in a `const` variable named `amountAsBigNumber`.

## Put it to the test

1. First, you should replace the last parameter that the `transfer` function takes (`ethers`) with `tokenSet`.
2. Let's update the second line of your function by replacing the argument passed to the `closestPackableTransactionAmount`.  Call the `tokenSet.parseToken` function to convert the `amountToTransfer` variable to `BigNumber`.
3. Similarly, on the third line, call the `tokenSet.parseToken` function to convert the `transferFee` variable to `BigNumber`.
