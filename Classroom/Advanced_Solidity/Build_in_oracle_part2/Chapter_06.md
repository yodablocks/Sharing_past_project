# Chapter 6: The Retry Loop

Now, retrieving the ETH price from the Binance public API comes with the following aspects which are worth paying attention to.

On one hand, suppose that you make a request but there's a network glitch. If so, the request will fail. If you just let that happen, the caller contract will have to reinitiate the whole process from the beginning, even if in a matter of seconds the network connectivity is restored. Yeah, this is not robust enough. Are we thinking of the same solution? Let's see. The way I'd go about this is to implement a retry mechanism.

So, on error, the application will start retrying. But, on the other hand, if there's a larger issue (like the address of the API has been changed), your app could get stuck in an infinite loop.

Thus, you'll need a condition that breaks the retry loop, if need be.

Similar to how you did in Chapter 4, you'll simply write a `while` block. But this time, you'll increment a variable on each pass and the loop will check whether that variable is `< MAX_RETRIES`.

See how simple this is?

## Put It to the Test

1. Define an `async function` called `processRequest`. As you already know, it takes four parameters: `oracleContract`, `ownerAddress`, `id`, and `callerAddress`.
2. The first line of the function should use `let` to declare a variable called `retries` and set it to `0`.
3. Declare a `while` loop that checks whether `retries < MAX_RETRIES`.
4. Let's now move inside of the `while` loop. Since a failed HTTP request `throw`s an error, you'll have to wrap the code that makes the call inside of a `try/catch` block like this:

  ```JavaScript
  try {
    // Do something
  } catch (error) {
    // Do some other thing
  }
  ```

Well, maybe that was a bit more complicated than you might've expected but I'm sure you did it without peeking at the answer🙌🏻.

You'll continue fleshing out this function in the next chapter.
