# Chapter 8: Fish Transfers

Question- Say Alice wants to send her fish to Bob. Shall we test this?

For sure!

If you've been following along with the previous lessons, you should know that, amongst other things, our fishes inherit from _ERC721_. And the _ERC721_ specification has 2 different ways to transfer tokens:

**(1)**

```
function transferFrom(address _from, address _to, uint256 _tokenId) external payable;
```

The first way has _Alice_ (the owner) calling `transferFrom` with her `address` as the `_from` parameter, Bob’s `address` as the `_to` parameter, and the `fishId` she wants to transfer.

**(2)**

```
function approve(address _approved, uint256 _tokenId) external payable;
```

followed by

```
function transferFrom(address _from, address _to, uint256 _tokenId) external payable;
```

The second way has Alice first calling `approve` with Bob’s address and the `fishId`. The contract then stores that Bob is approved to take the fish. Next, when Alice or Bob calls `transferFrom`, the contract checks if that `msg.sender` is equal to Alice’s or Bob’s address. If so, it transfers the fish to Bob.

We’ll call these two ways of transferring fish "scenarios". In order to test each scenario, we would want to create two different groups of tests and give them meaningful descriptions.

Why group them? We only have a few tests...

Yes, right now our logic is pretty straightforward, but this might not always be the case. Still, the second scenario (that is `approve` followed by `transferFrom`) requires at least two tests:

- first, we must check if Alice herself is able to transfer the fish.
    
- second, we also have to check if Bob is allowed to run `transferFrom`.
    

Moreover, in the future, you might want to add other functionalities that would require different tests. We believe it is best to put a scaleable structure in place from the very beginning😉. It makes understanding your code much easier for outsiders, or for yourself if you've spent time concentrating on something else for a little while.

> Note: If you end up in a position where you're working with other coders, you'll find they're more likely to follow whichever conventions you've laid down in your initial code. Being able to collaborate effectively is one of the key skills you'll need if you ever want to work on big, successful projects. Getting good habits that help you do this as early on as possible will make your life as a coder easier and more successful.

## The context function

To group tests, _Truffle_ provides a function called `context`. Let me quickly show you how to use it in order to better structure our code:

```
context("with the single-step transfer scenario", async () => {
    it("should transfer a fish", async () => {
      // TODO: Test the single-step transfer scenario.
    })
})

context("with the two-step transfer scenario", async () => {
    it("should approve and then transfer a fish when the approved address calls transferFrom", async () => {
      // TODO: Test the two-step scenario.  The approved address calls transferFrom
    })
    it("should approve and then transfer a fish when the owner calls transferFrom", async () => {
        // TODO: Test the two-step scenario.  The owner calls transferFrom
     })
})
```

If we add this to our `CryptoFish.js` file and then run `truffle test` the output would look similar to this:

```
Contract: CryptoFish
    ✓ should be able to create a new fish (100ms)
    ✓ should not allow two fishes (251ms)
    with the single-step transfer scenario
      ✓ should transfer a fish
    with the two-step transfer scenario
      ✓ should approve and then transfer a fish when the owner calls transferFrom
      ✓ should approve and then transfer a fish when the approved address calls transferFrom


  5 passing (2s)
```

Well?

Hmm...

Take a look again - there's an issue with the above output. It looks like all tests have passed which is obviously false since we didn't even write them yet!!

Fortunately, there's an easy solution- if we just place an `x` in front of the `context()` functions as follows: `xcontext()`, `Truffle` will skip those tests.

> Note: `x` can be placed in front of an `it()` function as well. Don't forget to remove all the x's when the tests for those functions have been written!

Now, let's run `truffle test`. The output should look something like this:

```
Contract: CryptoFish
    ✓ should be able to create a new fish (199ms)
    ✓ should not allow two fishes (175ms)
    with the single-step transfer scenario
      - should transfer a fish
    with the two-step transfer scenario
      - should approve and then transfer a fish when the owner calls transferFrom
      - should approve and then transfer a fish when the approved address calls transferFrom


  2 passing (827ms)
  3 pending
```

Where "-" represents a test that's been skipped with that "x" marker.

Pretty neat, huh? Now you can run your tests as you go along, and mark out empty functions where you know you will need to write tests in the near future.

# Put it to the test

1. Go ahead and copy/paste the code from above.
    
2. For now, let's _skip_ our new `context` functions.
    

Our tests are just empty shells and there is a lot of logic to be written in order to implement them. We'll do it in smaller pieces over the coming chapters.
