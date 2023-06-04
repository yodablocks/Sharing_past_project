# Chapter 8: Using Try and Catch in JavaScript

Great, you've finished coding the `try` block! Now, let's move to the `catch` block. Remember, these lines of code are executed if an exception is thrown in the `try` block.

The logic looks something like this:

* First, you'd want to determine if the maximum number of retries has been reached. To do so, you'll use an `if` statement similar to the one below:
  ```JavaScript
  if (condition) {
    doSomething()
  }
  ```

* If `condition` evaluates to `true`, meaning that the maximum number of retries has been reached, then you'd want to notify the contract that something happened, and the oracle can't return a valid response. The simplest way to do this is to call the `setLatestEthPrice` and pass it `0` as the ETH price.
* If `condition` evaluates to `false`, meaning that the maximum number of requests has not been reached, you'd just have to increment the number of retries.

This logic can be implemented in just a few lines of code. Let's make the following changes.

## Put It to the Test

1. Remember that the `retries` variable starts counting with the number `0`. Add an if statement comparing `retries` and `MAX_RETRIES - 1`. This is JavaScript, so let's use the strict comparison operator (`===`).
2. Inside of the `if` statement, run the `setLatestEthPrice` method just like you did in the previous chapter. Make sure you pass it `'0'` instead of `ethPrice`.
3. If the maximum number of retries has been reached, the next line should just `return`.
4. Outside of the `if` statement, use `++` to increment the `retries` variable.
