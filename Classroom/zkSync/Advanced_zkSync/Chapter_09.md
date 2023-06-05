# Chapter 9: Update the getFee function

We're close to being done here! Before we conclude, let's update the `getFee` function.

## Put it to the test

1. Replace the last parameter that the `getFee` function takes (`ethers`) with `tokenSet`.
2. The last line of your function should call the `tokenSet.formatToken` function to convert the `fee.totalFee` variable from `BigNumber` to a human-readable format. The function takes two parameters: `token` and `fee.totalFee`.

> 👉🏻 While we're here, note that we've gone ahead and updated the `src/bob.js` file. There are only a few minor changes but be sure to give it a read through.

This concludes our lesson. You now know how to build an application that allows users to interact with the zkSync protocol!
