> __Warning__ NOT FINISHED

# Chapter 1: Introduction

If you're new to **ADVANCE SOLIDITY**, it's highly recommended that you go over the first six lessons before starting this one. Please take the time to get familiar with writing a smart contract. Otherwise, it will be quite hard to follow this lesson.

## The Missing Piece

So you've worked your way through our previous lessons. Awesome! This means you've almost mastered the art of building DApps.

But an important piece of the puzzle is still missing.

That's right... you still have to learn how to deploy a smart contract.

Now, if you have a background in front-end development, you are probably well accustomed to the multitude of tools like _Webpack, Gulp, or Browserify_ that make a developer's life simpler.

But what tools do **Solidity** developers use?

## Truffle

**_Truffle_** is the most popular blockchain development framework for good reason - it's packed with lots of useful features:

* easy smart contract compilation
* automated ABI generation
* integrated smart contract testing - there's even support for **Mocha** and **Chai**!
* support for multiple networks - code can be deployed to Rinkeby, **_Ethereum_** or even to **_Loom_**. We'll walk you through this later😉

Provided that `npm` and `node` have been installed on your computer, we'll want you to install **Truffle** and make it available globally.

# Put It to the Test

We'll start with the basics. Fire up a new terminal window, create a directory called `CryptoZombies`, and `cd` into it.

1. Now, let's install **Truffle** and make it available globally.
    
    > Note: Here's how you can use `npm` to install a package and make it available globally:
    
    ```
    npm install package_name -g
    ```
