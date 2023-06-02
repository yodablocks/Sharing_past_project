# Chapter 2: Getting Set Up

Let's move forward. In this chapter, we're going to continue setting things up so we can write and run our tests.

## Build Artifacts

Every time you compile a smart contract, the _Solidity_ compiler generates a JSON file (referred to as **build artifacts**) which contains the binary representation of that contract and saves it in the `build/contracts` folder.

Next, when you run a migration, _Truffle_ updates this file with the information related to that network.

The first thing you'll need to do every time you start writing a new test suite is to load the build artifacts of the contract you want to interact with. This way, **Truffle** will know how to format our function calls in a way the contract will understand.

Let's look at a simple example.

Say there was a contract called `MyAwesomeContract`. We could do something like the following to load the build artifacts:

```
const MyAwesomeContract = artifacts.require(“MyAwesomeContract”);
```

The function returns something called a **_contract abstraction_**. In a nutshell, a _contract abstraction_ hides the complexity of interacting with **Ethereum** and provides a convenient _JavaScript_ interface to our _Solidity_ smart contract. We'll be using it in the next chapters.

### The contract() function

Behind the scenes, **Truffle** adds a thin wrapper around **Mocha** in order to make testing simpler. Since our course focuses on **Ethereum** development, we won't be spending much time explaining the bits and bytes of _Mocha_. If you're inclined to learn more about _Mocha_, check out [their website](https://mochajs.org/), once you're done with this lesson. For now, you only have to understand what we cover here - how to:

- **group tests** by calling a function named `contract()`. It extends **Mocha**'s `describe()` by providing a **list of accounts for testing** and doing some cleanup as well.
    
    `contract()` takes two arguments. The first one, a `string`, must indicate what we’re going to test. The second parameter, a `callback`, is where we’re going to actually write our tests.
    
- **execute them**: the way we’ll be doing this is by calling a function named `it()` which also takes two arguments: a `string` that describes what the test actually does and a `callback`.
    

Putting it together, here's a bare-bones test:

```
 contract("MyAwesomeContract", (accounts) => {
   it("should be able to receive Ethers", () => {
   })
 })
```

> Note: A well-thought test explains what the code actually does. Make sure the description of the test suite and the test case can be read together as a **coherent statement**. It’s like you’re writing documentation.

Every test you’ll want to write follows this simple pattern. Pretty easy, isn't it?😁

# Put it to the test

Now that we've created an empty `CryptoFish.js` file, let's fill it in.

1. The first line of code should declare a `const` named `CryptoFish` and set it equal to the result of the `artifacts.require` function with the name of the contract we want to test as an argument.
    
2. Next, go ahead and copy/paste the test from above.
    
3. Change the way we're calling `contract()` such that the first parameter is the name of our smart contract.
    
    > Note: Don't worry about the `accounts` argument. We'll explain it in the next chapter.
    
4. The first parameter passed to the `it()` function (in our example, that is "should be able to receive Ethers") should be the name of our test. Since we'll start with creating a new fish, make sure that the first parameter is set to "should be able to create a new fish".
    

We're all set. Let's move to the next chapter.
