# Chapter 4: The Logical NOT Operator

In this lesson, you're going to continue to flesh out the `addOracle` function.

As we've seen in the first lesson, the `Roles` smart contract implements three functions: `add`, `remove`, and `has`.

## The Logical NOT Operator

To make sure that an address is not already an oracle, you'll have to use the logical NOT operator (`!`). Simply put, `!` negates its parameter. So, if `oracles.has(_owner)` evaluates to `true`, then `!oracles.has(owner)` evaluates to false.

With that said, let's continue fleshing out the `addOracle` function.

## Put It to the Test

1. Add a `require` statement that makes sure `_oracle` is not already an oracle. If it's an oracle, set the error message to `"Already an oracle!"`.
2. Call the `oracles.add` function passing it `_oracle` as a parameter.
3. There is one more thing to do before you wrap up this function. Let's fire an `AddOracleEvent`. It takes one parameter - the address of the newly added oracle which comes from the function's parameters.
