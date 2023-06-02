# Chapter 11: ERC721 Token Transfers- Two Step Scenario

We're close to being done with testing the transfers! Let's now test the scenario in which Alice calls `transferFrom`.

We have some good news for you- this test is straightforward. All you have to do is to copy and paste the code from the previous chapter and make it so that **Alice** (not Bob) calls `transferFrom`:

# Put it to the test

1. Copy and paste the code from the previous test and have Alice call `transferFrom`.
2. "Unskip" it and we're all set.

If you run `truffle test` the output would look similar to this:

```
Contract: CryptoFish
    ✓ should be able to create a new fish (201ms)
    ✓ should not allow two fishes (486ms)
    ✓ should return the correct owner (382ms)
    with the single-step transfer scenario
      ✓ should transfer a fish (337ms)
    with the two-step transfer scenario
      ✓ should approve and then transfer a fish when the approved address calls transferFrom (266ms)
  5 passing (3s)
```

I can't think of anything else to test that's related to transfers, so we're done for now.
