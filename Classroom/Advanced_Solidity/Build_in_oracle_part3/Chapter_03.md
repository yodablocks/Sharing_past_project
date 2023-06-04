# Chapter 3: Setting Up New Oracles

Great! Now it's time to write the function that sets up a new oracle by adding its address to the list of known oracles. You might think this is just a matter of calling the `oracles.add` function with the address of the oracle you want to add as an argument.

Well... think again. Before doing that you'll want to:

*  Verify that the caller is the owner of the contract.
*  Make sure that the address is not already an oracle.
*  Notify the front-end that a new oracle has been added by firing an event at the end of the function.

## Put It to the Test

1. Declare an event called `AddOracleEvent`. It takes one parameter (`oracleAddress`) of type `address`.
2. Next, let's define a function called `addOracle`. It's a `public` function, and it takes an `address` parameter called `_oracle`.
3. Add a `require` statement to make sure `owners` contains `msg.sender` (hint: use `owners.has`). The second parameter should be `"Not an owner!"`.

We'll continue fleshing out this function in the next chapter!
