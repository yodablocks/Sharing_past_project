# Chapter 12: Fish Attacks

Wow! The previous chapters were pretty information-dense, but we covered a lot of ground.

So are we done now with all the scenarios? No, we're not there yet; we've left the best stuff for the end.

We've built a fish game and **the best part** is where fish fight each other, right?

This test is pretty straightforward and consists of the following steps:

- **First**, we're going to be creating two new fishes - one for Alice and the other one for Bob.
- **Second**, Alice will run `attack` on her fish with Bob's `fishId` as a parameter
- **Finally**, for the test to pass, we are going to check if `result.receipt.status` equals `true`

While we're here, let's say I've quickly coded all this logic, wrapped it in an `it()` function, and run `truffle test`.

Then, the output would look something like this:

```
Contract: CryptoFish
    ✓ should be able to create a new fish (102ms)
    ✓ should not allow two fishes (321ms)
    ✓ should return the correct owner (333ms)
    1) fishes should be able to attack another fish
    with the single-step transfer scenario
      ✓ should transfer a fish (307ms)
    with the two-step transfer scenario
      ✓ should approve and then transfer a fish when the approved address calls transferFrom (357ms)


  5 passing (7s)
  1 failing

  1) Contract: CryptoFish
       fishes should be able to attack another fish:
     Error: Returned error: VM Exception while processing transaction: revert

```

Uh oh. Our test just failed☹️.

But why?

Let's figure it out. First, we're going to take a closer look at the code behind `createRandomFish()`:

```
function createRandomFish(string _name) public {
  require(ownerFishCount[msg.sender] == 0);
  uint randDna = _generateRandomDna(_name);
  randDna = randDna - randDna % 100;
  _createFish(_name, randDna);
}
```

So far so good. Moving forward, let's dig into `_createFish()`:

```
function _createFish(string _name, uint _dna) internal {
  uint id = zfishes.push(Fish(_name, _dna, 1, uint32(now + cooldownTime), 0, 0)) - 1;
  fishToOwner[id] = msg.sender;
  ownerFishCount[msg.sender] = ownerFishCount[msg.sender].add(1);
  emit NewFish(id, _name, _dna);
}
```

Ohh, you see the issue?

Our test failed because we've added a **cooldown** period to our game, and made it so fishies have to wait **1 day** after attacking (or feeding) to attack again.

Without this, the fish could attack and multiply countless times per day, which would make the game way too easy.

Now, what should we do now... wait for a day?

## Time Travelling

Fortunately, we don't have to wait that much. In fact, there's no need to wait at all. That's because _Ganache_ provides a way to move forward in time through two helper functions:

- `evm_increaseTime`: increases the time for the next block.
- `evm_mine`: mines a new block.

You don't even need a DeLorean for this kind of time travel.

Let me explain how these functions work:

- Every time a new block gets mined, the miner adds a timestamp to it. Let's say the transactions that created our fishes got mined in block 5.
    
- Next, we call `evm_increaseTime` but, since the blockchain is immutable, there is no way of modifying an existing block. So, when the contract checks the time, it will not be increased.
    
- If we run `evm_mine`, block number 6 gets mined (and timestamped) which means that, when we put the fishes to fight, the smart contract will "see" that a day has passed.
    

Putting it together, we can fix our test by traveling through time as follows:

```
await web3.currentProvider.sendAsync({
  jsonrpc: "2.0",
  method: "evm_increaseTime",
  params: [86400],  // there are 86400 seconds in a day
  id: new Date().getTime()
}, () => { });

web3.currentProvider.send({
    jsonrpc: '2.0',
    method: 'evm_mine',
    params: [],
    id: new Date().getTime()
});
```

Yeah, that’s a nice piece of code, but we wouldn’t want to add this logic to our `CryptoFish.js` file.

We’ve gone ahead and moved everything to a new file named `helpers/time.js`. To increase the time, you'll simply have to call: `time.increaseTime(86400);`

Yeah, still not good enough. After all, do we really expect you to know how many seconds there are in a day right off the top of your head?

Of course not. This is why we’ve added another _helper function_ named `days` that takes the number of days we want to increase time with as an argument. You would call this function like so: `await time.increase(time.duration.days(1))`

> Note: Obviously, time traveling is not available on the main net or on any of the available test chains that are secured by miners. It would make a real mess of things if anyone could just choose to change how time operates in the real world! For testing smart contracts, time travel can be an essential part of the coder's repertoire.

# Put it to the test

We've gone ahead and filled in the version of the test that fails.

1. Scroll down to the comment we've left for you. Next, fix the test case by running `await time.increase` as shown above.

We're all set now. Let's run `truffle test`:

```
Contract: CryptoFish
    ✓ should be able to create a new fish (119ms)
    ✓ should not allow two fishes (112ms)
    ✓ should return the correct owner (109ms)
    ✓ fishes should be able to attack another fish (475ms)
    with the single-step transfer scenario
      ✓ should transfer a fish (235ms)
    with the two-step transfer scenario
      ✓ should approve and then transfer a fish when the owner calls transferFrom (181ms)
      ✓ should approve and then transfer a fish when the approved address calls transferFrom (152ms)
```

And there you go! That's the final step of this chapter.
