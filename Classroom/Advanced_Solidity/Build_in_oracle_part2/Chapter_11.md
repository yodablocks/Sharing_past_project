# Chapter 11: Wrapping Up the Oracle

We're closer to being done with the oracle contract. Now it's time to write the code that ties everything together. Remember that, due to JavaScript's single-threaded nature, we're processing the queue in batches and our thread will just `sleep` for `SLEEP_INTERVAL` milliseconds between each iteration. For this, we'll use the `setInterval` function. The following example repeatedly "does something", with a predetermined delay between each iteration:

```JavaScript
setInterval(async () => {
 doSomething()
}, SLEEP_INTERVAL)
```

Next, we'd want to provide a way for the user to gracefully shut down the oracle. This can be done by catching the `SIGINT` handler like this:

```JavaScript
process.on( 'SIGINT', () => {
 // Gracefully shut down the oracle
 })
```

## Put It to the Test

We've gone ahead and filled in almost everything, you just need to add a few small touches.

1. You don't want to leave a dangling `client` instance, do you? Inside of the callback function that gets executed on `SIGINT`, call the `client.disconnect` function. It doesn't take any parameters.

2. Inside of the function that gets executed every SLEEP_INTERVAL milliseconds, `await` for `processQueue`. The function takes two parameters: `oracleContract` and `ownerAddress`.

This concludes the oracle implementation but we're not done yet. Next, we'll build a simple client and then we'll show you how to deploy and run your oracle.
