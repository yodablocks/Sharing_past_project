# Chapter 7: Using Try and Catch in JavaScript

In the previous chapter, you've added a `try/catch` block to the `processRequest` function.

Before moving on with the code, let's spend a few minutes looking into how `try/catch` works in JavaScript.

Well, the way this works is that the code inside of the `try` block gets executed and tested for errors. If an exception is thrown, the execution of the code inside of the `try` block stops, and the computer "jumps" to the lines of code inside of the `catch` block.

> Note that JavaScript allows you to write code that executes no matter whether an exception is thrown inside of the `try` block. These lines of codes should be placed inside of a `finally` block. You won't use it in this tutorial, but you never know when it comes in handy🤓.

With that being said, let's focus back on what the `processRequest` function should do. So, inside of the `try` block, it should `retrieveLatestEthPrice` and then call the oracle contract to set the latest ETH price.

## Put It to the Test

1. The first line of the `try` block should simply `await` a function called `retrieveLatestEthPrice`, and then store the result in a `const` called `ethPrice`. The function takes no parameters. This is the function that actually "talks" with the Binance public API. We'll explain it later in  this lesson.
2. Now, the second line of code could call the `setLatestEthPrice` method of the `oracleContract` but, before that, you must massage the data a bit. To make the code easier to read and maintain, you'll write a separate function for that. For now, let's just call it like so:
  ```JavaScript
  await setLatestEthPrice(oracleContract, callerAddress, ownerAddress, ethPrice, id)
  ```
3. The third line of the `try` block should just call `return`.
