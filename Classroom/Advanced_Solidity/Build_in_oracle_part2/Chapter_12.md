# Chapter 12: Returning multiple values in JavaScript

You've just finished implementing the oracle! That's nothing short of amazing🤘🏻

Now it's time to build a bare-bones client that interacts with the oracle.

This chapter is intentionally kept short because you're already familiar with most of the logic, and we don't want to take much of your time doing repetitive stuff.

We've created a new tab for the `Client.js` file and placed almost everything you need into a file called `Client.js`. Give it a read-through before moving on.

## Put It to the Test

You only have to add the line of code that calls the `updateEthPrice` method of the `callerContract`. We've left a comment to indicate where you should start.

1. Inside of the function that gets called by `setInterval`, execute `callerContract.methods.updateEthPrice`. Remember that it's an `async` function so you'll have to prepend the `await` keyword to the function call. Then, chain a `send` function call. This function takes one parameter: `{ from: ownerAddress }`.

>Note: Here's a simple example of how you can chain two functions in JavaScript: `firstFunction().secondFunction()`. The way this works is that `firstFunction` returns an object that implements `secondFunction()`.
