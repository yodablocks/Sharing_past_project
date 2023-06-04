# Chapter 7: Computing the ETH Price

As long as the smart contract expected only one answer, passing the response to the caller was just a matter of calling the `callerContractInstance.callback` function as follows:

```Solidity
callerContractInstance.callback(_ethPrice, _id);
```

But now, there will be up to `numOracles` responses for each request. And the trick here is that a smart contract can't initiate an action by itself. To put it in other words, there's no way you can use a similar construct like the one you've used in the JavaScript component of the oracle:

```JavaScript
setInterval(async () => {
  doSomething()
}, SLEEP_INTERVAL)
```

Instead, the smart contract needs to be triggered somehow.

And in this case, the trigger is the call to the `setLatestEthPrice` function. That said, instead of answering when's the right time to compute the ETH price, you should answer a different question - how many responses are enough for the oracle to compute the ETH price and pass it to the client.

You might be tempted to say that the contract should wait until `numOracles` responses are submitted. In other words, the contract should wait for every oracle to submit a response. But let's look deeper into it.

At any given time, an oracle can be taken down for maintenance. Or it can lose its network connectivity. If any of these happen, your contract will not be able to fulfill any requests until the aforementioned issues are fixed.

A more flexible method would be to define a threshold, and when the number of responses equals this threshold, then the smart contract will calculate the ETH price and pass it to the caller. For sure, this method isn't bullet-proof either, but it does a better job mitigating possible issues.

## Put It to the Test

We've gone ahead and defined a variable called `THRESHOLD`, and then fleshed out a function that lets you set its value. Now let's move to the `setLatestEthPrice` function.

1. Below the line of code that `push`es `resp`, define a variable called `numResponses`. Set it equal to the length of the `requestIdToResponse[_id]` array.
  > In Solidity you can retrieve the length of an array like so:
  ```Solidity
  uint myArray[10];
  uint length = myArray.length
  ```
2. Add an `if` statement comparing `numResponses` and `THRESHOLD`.
  > In Solidity, the syntax of the `if` statement is as follows:
  ```Solidity
  if (firstValue == secondValue) {
    doSomething();
  }
  ```
  Simply put, if `firstValue == secondValue` evaluates to `true`, the code enclosed in the curly braces is executed. If the expression evaluates to false, then the body of the statement is skipped.

3.  Move the block delimited by the following lines of code inside the if statement:

  **starts with:**

  ```Solidity
  delete pendingRequests[_id];
  ```

  **ends with:**

  ```Solidity
  emit SetLatestEthPriceEvent(computedEthPrice, _callerAddress);
  ```
