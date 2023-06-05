# Chapter 5: Update the depositToZkSync function


Great, you've finished updating the `alice.js` file!
Now, let's move to the `utils.js` file and update the `depositToZkSync` function.


## Put it to the test

1. The `depositToZkSync` function should use the `tokenSet` object to convert the `amountToDeposit` variable from a human-readable form to `BigNumber`. Update the line of code that declares this function, replacing the last parameter (`ethers`) with `tokenSet`.
2. The `zkSyncWallet.depositToSyncFromEthereum` function takes one parameter - an object. Set the value of the the `amount` property to `tokenSet.parseToken(token, amountToDeposit)`.
