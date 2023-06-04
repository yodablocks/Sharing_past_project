# Chapter 4: Looping Trough the Processing Queue

Having coded the function that adds a new request whenever the oracle contract fires `GetLatestEthPriceEvent`, the next thing on your list should be to process these requests.

Imagine there are a bunch of caller contracts sending requests to your oracle. Processing the `pendingRequests` array in Node.js could be problematic for a very simple reason: JavaScript is single-threaded. This means that all other operations would be blocked until the processing is finished.

A technique to solve this problem is to break the array into smaller chunks (up to `MAX_CHUNK_SIZE`), and process these chunks individually. To simplify things, after each chunk, the application will `sleep` for `SLEEP_INTERVAL` milliseconds.

You'll implement this with a `while` loop.

A `while` loop is comprised of a condition that's evaluated at every pass and the code that gets executed. The condition is enclosed in parentheses and the code is enclosed in curly brackets:

```JavaScript
let counter = 0
while ( counter <= 10 ) {
  console.log(counter)
  counter++
}
```

But what if two conditions must be met for the code in the curly brackets to be executed? If so, you can test for two conditions (or more than two if you want), by chaining them using the logical `AND` operator (`&&`):

```JavaScript
let counter = 0
while ( counter <= 10 && isNotMonday) {
  console.log(counter)
  counter++
}
```

Let's make the function that breaks this array into smaller pieces.

## Put It to the Test

1. Declare a function named `processQueue`. It's an `async` function and takes two parameters: `oracleContract` and `ownerAddress`.
2. The function should first declare a variable called `processedRequests` and set it to `0`. You'll change the value of this variable later. This means you must use `let` instead of `const`.
3. Declare a `while` loop with the condition checking that:

   * There are pending requests in the queue. You can check this by testing whether `pendingRequests.length` is `> 0` or not.

    and (`&&`)

   * The `processedRequests` variable is `< CHUNK_SIZE`.

You'll continue fleshing out this function in the next chapter.
