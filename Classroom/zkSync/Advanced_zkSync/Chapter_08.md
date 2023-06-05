# Chapter 8: Update the withdrawToEthereum function

In this chapter, you're going to update the `withdrawToEthereum` function to use the `tokenSet` object.

The steps are similar to those we've explained in the previous section, so we won't spend time repeating what you should have learned already.

## Put it to the test

1. First, you should replace the last parameter that the `withdrawToEthereum` function takes (`ethers`) with `tokenSet`.
2. Let's update the second line of your function by replacing the argument passed to the `closestPackableTransactionAmount` function.  Call the `tokenSet.parseToken` function to convert the `amountToWithdraw` variable to `BigNumber`.
3. Similarly, on the third line, call the `tokenSet.parseToken` function to convert the `withdrawalFee` variable to `BigNumber`.


