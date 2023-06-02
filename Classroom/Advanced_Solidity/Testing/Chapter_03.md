# Chapter 3: The First Test- Creating a New Fish

Before deploying to **Ethereum**, it is best to test your smart contracts locally.

You can do so by using a tool called [Ganache](https://truffleframework.com/ganache), which sets up a local **Ethereum** network.

Every time _Ganache_ starts, it creates 10 test accounts and gives them 100 Ethers to make testing easier. Since _Ganache_ and _Truffle_ are tightly integrated we can access these accounts through the `accounts` array we've mentioned in the previous chapter.

But using `accounts[0]` and `accounts[1]` would not make our tests read well, right?

To aid comprehension, we'd like to use two placeholder names- Alice and Bob. So, inside the `contract()` function, let's initialize them like so:

```
let [alice, bob] = accounts;
```

> Note: Forgive the poor grammar. In _JavaScript_, the convention is to use lowercase for variable names.

Why Alice and Bob? There is a big tradition that makes Alice and Bob or "A and B" common names used in cryptography, physics, programming, and more. It's a short but interesting history, and well worth a [read](http://cryptocouple.com/) after you complete this lesson.

Now let's move on to our first test.

## Creating a New Fish

Say Alice wants to play our awesome game. If so, the first thing she would want to do is to **create her own fish 🐠**. To do that, the front-end (or _Truffle_ in our case) would have to call the `createRandomFish` function.

> Note: As a review, here is the _Solidity_ code in our contract:

```
 function createRandomFish(string _name) public {
   require(ownerFishCount[msg.sender] == 0);
   uint randDna = _generateRandomDna(_name);
   randDna = randDna - randDna % 100;
   _createFish(_name, randDna);
 }
```

We begin by testing this function.

# Put it to the test

1. The first line of the `contract()` function should declare two variables named `alice` and `bob` and initialize them as shown above.
    
2. Next, we would want to properly call the `it()` function. The second parameter (a `callback` function) is going to "talk" to the blockchain, which means that the function is asynchronous. Just prepend the `async` keyword. This way, every time this function gets called with the `await` keyword, our test waits for it to return.
    

> Explaining how promises work is out of the scope of this lesson. Once you've finished this lesson, feel free check out the [official documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) to further your knowledge.
