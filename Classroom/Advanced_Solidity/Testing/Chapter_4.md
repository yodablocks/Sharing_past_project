# Chapter 4: The First Test- Creating a New Fish

Great job! Now that we have a shell for our first test, let me walk you through how testing works.

Usually, every test has the following phases:

1. **_set up_**: in which we define the initial state and initialize the inputs.
    
2. **_act_**: where we actually test the code. Always make sure you _test only one thing_.
    
3. **_assert_:** where we check the results.
    

Lets look at what our test should do in some more detail.

## 1. Set up

In Chapter 2, you learned to create a _contract abstraction_. However, a _contract abstraction_, as its name says, is just an abstraction. In order to actually interact with our smart contract, we have to create a _JavaScript_ object that will act as an **instance** of the contract. Continuing our example with `MyAwesomeContract`, we can use the _contract abstraction_ to initialize our instance like this:

```
const contractInstance = await MyAwesomeContract.new();
```

Good, so what's next?

Calling `createRandomFish` requires us to pass it the fish's name as a parameter. So, the next step would be to give a name to Alice's fish. Something like “Alice’s Awesome Fish”.

However, if we do this for each test, our code is not going to look pretty. A better approach is to initialize a global array as follows:

```
const fishNames = ["Fish #1", "Fish #2"];
```

And then, call the contract's methods like so:

```
contractInstance.createRandomFish(fishNames[0]);
```

> Note: Using an array to store fish' names comes in handy if you want, for example, to write a test that creates 1000 fishes instead of just one or two😉.

# Put it to the test

We've gone ahead and initialized the `fishNames` array for you.

1. Let's create an instance of our contract. Declare a new `const` named `contractInstance`, and set it equal to the result of the `CryptoFish.new()` function.
    
2. `CryptoFish.new()` "talks" to the blockchain. This means that it's an asynchronous function. Let's add the `await` keyword before the function call.
