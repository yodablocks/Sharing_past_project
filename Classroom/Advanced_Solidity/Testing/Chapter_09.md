# Chapter 9: ERC721 Token Transfers- Single Step Scenario

So far we’ve merely been warming up...

But now it's time to really show off what you know!

In the next chapters, we're going to be putting what we’ve learned together and test something really cool.

To begin with, we're going to be testing the scenario in which _Alice_ transfers her ERC721 token to _Bob_, in a single step.

Here is what our test should do:

- Create a new fish for Alice (Remember that a fish is nothing more than an ERC721 token).
    
- Make it so that Alice transfers her ERC721 token to Bob.
    
- At this point, Bob should own the ERC721 token. If so, `ownerOf` would return a value that is equal to Bob's address.
    
- Let's wrap it up by checking if Bob is the `newOwner`, inside an `assert`.
    

# Put it to the test

1. The first line of the function should call `createRandomFish`. Give it `fishNames[0]` as the name and make sure Alice is the owner.
    
2. The second line should declare a `const` named `fishId` and set it equal to the fish's id. In Chapter 5, you learned how to retrieve information from logs and events our smart contract. Refresh your memory, if needed. Make sure you also convert `fishId` to a valid number with `toNumber()`.
    
3. Then, we have to call `transferFrom` with `alice` and `bob` as the first parameters. Make sure Alice calls this function and we're `await`ing for it to finish running before moving to the next step.
    
4. Declare a `const` called `newOwner`. Set it equal to `ownerOf` called with `fishId`.
    
5. Lastly, let's check whether Bob owns this ERC721 token. Putting this into code, it means we should run `assert.equal` with `newOwner` and `bob` as parameters;
    
    > Note: `assert.equal(newOwner, bob)` and `assert.equal(bob, newOwner)` are basically the same thing. But our command line interpreter is not too advanced, so it won't consider your answer correct unless you type the first option.
    
6. Did I say the previous step is the last one! Well... it was a lie. The last thing we want to do is to "unskip" the first scenario by removing the `x`.
    

Phew! That's a lot of code. Hope you manage to get it right. If not, feel free to click "show answer".

Now let's run `truffle test` and see if our new test passes:

```
Contract: CryptoFish
  ✓ should be able to create a new fish (146ms)
  ✓ should not allow two fishes (235ms)
  with the single-step transfer scenario
    ✓ should transfer a fish (382ms)
  with the two-step transfer scenario
    - should approve and then transfer a fish when the owner calls transferFrom
    - should approve and then transfer a fish when the approved address calls transferFrom


3 passing (1s)
2 pending
```

And there it is! Our code passed the test with flying colors.

In the next chapter, we are going to move on to the 2 step scenario in which `approve` is followed by `transferFrom`.
