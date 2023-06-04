# Chapter 5: Removing an Oracle

Great! You've successfully implemented the function that adds an oracle. Now, you'll need a function that removes an oracle. The logic should follow along the same lines as the `addOracle` function.

But there's more to it.

What would happen if you remove the last oracle by mistake? Yeah, the smart contract will be rendered useless until you figure out what has happened. Thus, more like a safety net, you'll want to keep track of the number of oracles. The way this would work is pretty simple: first, you'll define a new variable called `numOracles`. Then, every time an oracle is added, the `addOracle` function will increment this variable.  Inside the function that removes an oracle, you'll first have to use a `require` statement to make sure `numOracles > 1`. If this evaluates to `true`, then you call the `oracles.remove` function, and decrement `numOracles`.

## Put It to the Test

We've gone ahead and created a function named `removeOracle`, and filled in the first two lines of code, making sure that `msg.sender` is the owner of the contract, and `_oracle` (the `address` passed as a parameter) is in the list of oracles.

1. Create a `uint` variable named `numOracles` and initialize it with `0`. Make it `private`.
2. Declare an event called `RemoveOracleEvent`. It takes one parameter called `oracleAddress` of type `address`.
3. Inside the `removeOracle` function, add the `require` statement that checks that `numOracles > 1`. Set the message to `"Do not remove the last oracle!"`
4. Call the `oracles.remove` function, passing it `_oracle` as an argument.
5. Use `--` to decrement `numOracles`.
6. Lastly, let's fire `RemoveOracleEvent`. It takes one argument- `_oracle`.

This was a lot. And still, there's one thing left. The `addOracle` function should increment the `numOracles` variable. Don't worry about this though, we've gone ahead and added that line of code🤓.
