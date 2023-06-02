# Chapter 7: Keeping the Fun in the Game 

In this chapter, we're going to fill in the body of our second test. Here's what it should do:

- First, Alice should call `createRandomFish` and give it `fishNames[0]` as the name of her first fish.
- Next, Alice should try to create her second fish. The only thing that's different is that this time, the fish name should be set to `fishNames[1]`.
- At this point, we expect the contract to `throw` an error.
- Since our test should pass only if the smart contract errors out, our logic will look a bit different. We’ll have to wrap the second `createRandomFish function call inside of a `try/catch` block as follows:

```
try {
    //try to create the second fish
    await contractInstance.createRandomFish(fishNames[1], {from: alice});
    assert(true);
  }
  catch (err) {
    return;
  }
assert(false, "The contract did not throw.");
```

Now we've got exactly what we wanted, right?

Hmmm... we're pretty close but not quite there.

In order to keep our tests nice and tidy we've moved the code above to `helpers/utils.js` and imported it into “CryptoFish.js” like so:

```
const utils = require("./helpers/utils");
```

And this is how the line of code that calls the function should look like:

```
await utils.shouldThrow(myAwesomeContractInstance.myAwesomeFunction());
```

# Put it to the test

In the previous chapter, we've created an empty shell for our second test. Let's fill it in.

1. First, let's have Alice create her first fish. Give it `fishNames[0]` as the name and don't forget to properly set the owner.
    
2. After Alice created her first fish, run `shouldThrow` with `createRandomFish` as the parameter. If you can't remember the syntax for doing this, check the example from above. But first, try to do it without peeking.
    

Awesome, you've just finished writing your second test!

Now, we've gone ahead and run `truffle test` for you. Here's the output:

```
Contract: CryptoFish
    ✓ should be able to create a new fish (129ms)
    ✓ should not allow two fishes (148ms)


  2 passing (1s)
```

The test passed. 🍾
