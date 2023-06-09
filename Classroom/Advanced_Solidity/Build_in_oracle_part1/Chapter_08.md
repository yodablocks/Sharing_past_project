# Chapter 8: The getLatestEthPrice Function


Great job! You've just finished implementing the caller smart contract💪🏻💪🏻💪🏻.

Now it's time to move forward to the oracle contract. Let's start by taking a look into what this contract should do.

The gist of it is that the oracle contract acts as a bridge, enabling the caller contracts to access the ETH price feed. To achieve this, it just implements two functions: `getLatestEthPrice` and `setLatestEthPrice`.

## The getLatestEthPrice Function

To allow the callers to track their requests, the ``getLatestEthPrice`` function should first compute the request `id` and, for security reasons, this number should be hard to guess.

What security reasons, you ask?

In the third lesson, you're going to make the oracle more decentralized. Generating a unique id makes it harder for oracles to collude and manipulate the price for a particular request.

In other words, you would want to generate a **random number**.

But how can you generate a random number in Solidity?

One solution would be to let loose a fish on a keyboard. But the poor fish will also type spaces and letters so your "random number" will end up looking like this: `erkljf3r4398r4390r830`.

So, even if no fishes were hurt in the making of this lesson, that solution for generating a random number is simply not good enough😎.

However, in Solidity, you can compute a "good-enough" random number using the `keccak256` function like this:

```solidity
uint randNonce = 0;
uint modulus = 1000;
uint randomNumber = uint(keccak256(abi.encodePacked(now, msg.sender, randNonce))) % modulus;

```

The above takes the timestamp of `now`, the `msg.sender`, and an incrementing `nonce` (a number that is only ever used once, so we don't run the same hash function with the same input parameters twice). Then it packs the inputs and uses `keccak256` to convert them to a random hash. Next, it converts the hash to a `uint`. Finally, it uses `% modulus` to take only the last 3 digits. This gives you a "good-enough" random number between 0 and `modulus`.

> Lesson 4 explains why this approach is not 100% secure and provides a few alternatives for generating truly secure random numbers. Give it a read once you've finished this lesson.

## Put It to the Test

We've created a shell for the `EthPriceOracle` contract. Take a quick browse through the code before continuing. Note that your contract is `Ownable` and we've also included the content of the `CallerContractInterface.sol` file.

1. At the bottom of your contract, define a function named `getLatestEthPrice` that returns a `uint256`. It should be a `public` function.
2. On the first line, use `randNonce++` to increment `randNonce`.
3. Compute a random number between 0 and `modulus`, and store the result in a `uint` called `id`. If you get stuck, feel free to take a look at the example above where we generated a random number😉. Your solution should be similar.

You'll continue fleshing out the `getLatestEthPrice` function in the next chapter.
