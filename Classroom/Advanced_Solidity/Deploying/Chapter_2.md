# Chapter 2: Getting Started with Truffle

Now that we've installed **Truffle**, it's time to initialize our new project by running `truffle init`. All it is doing is to create a set of folders and config files with the following structure:

```
├── contracts
    ├── Migrations.sol
├── migrations
    ├── 1_initial_migration.js
└── test
truffle-config.js
truffle.js
```

Contracts, migrations, tests... this is pretty complicate

Don't worry, learning to use **Truffle** won't eat your brains. This chapter will walk you through **Truffle**'s default project structure, and once you know how to use **Truffle**, deploying smart contracts will be a breeze.

## Truffle's Default Directory Structure

So, running the `truffle init` command inside of the `CryptoFish` directory, should create several directories and some JavaScript and Solidity files. Let's have a closer look:

- **_contracts_**: this is the place where **Truffle** expects to find all our smart contracts. To keep the code organized, we can even create nested folders such as `contracts/tokens`. Pretty neat😉.
    
    > Note: `truffle init` should automatically create a contract called `Migrations.sol` and the corresponding migration file. We'll explain them a bit later.
    
- **_migrations_**: a migration is a JavaScript file that tells **Truffle** how to deploy a smart contract.
    
- **_test_**: here we are expected to put the unit tests which will be JavaScript or Solidity files. Remember, once a contract is deployed it can't be changed, making it essential that we test our smart contracts before we deploy them.
    
- **_truffle.js_** and **_truffle-config.js_**: config files used to store the network settings for deployment. **Truffle** needs two config files because on Windows having both `truffle.js` and `truffle.exe` in the same folder might generate conflicts. Long story short - if you are running Windows, it is advised to delete `truffle.js` and use `truffle-config.js` as the default config file. Check out **Truffle**'s [official documentation](https://truffleframework.com/docs/truffle/reference/configuration) to further your understanding.
    

But why should I use this directory structure? I'm not used to it and it looks complicated...

Well, there's are a few good reasons. First, **Truffle** will not work as expected if you change the names of these folders.

Second, by adhering to this convention your projects will be easily understood by other developers. To put it short, using a standard folder structures and code conventions make it easier if you expand or change your team in the future.

## truffle-hdwallet-provider

In this lesson, we will be using _Infura_ to deploy our code to **_Ethereum_**. This way, we can run the application without needing to set up our own **_Ethereum_** node or wallet. However, to keep things secure, _Infura_ does not manage the private keys, which means it can't sign transactions on our behalf. Since deploying a smart contract requires **Truffle** to sign transactions, we are going to need a tool called `truffle-hdwallet-provider`. Its only purpose is to handle the transaction signing.

> Note: Maybe you are asking why we chose not to install `truffle-hdwallet-provider` in the previous chapter using something like:

```
 npm install truffle truffle-hdwallet-provider
```

Well... the `truffle init` command expects to find an empty directory. If there's any file there, it will error out. Thus, we need to do everything in the correct order and install `truffle-hdwallet-provider` after we run `truffle init`.

# Put it to the test:

1. Run `truffle init`. This command generates the directory structure that we've discussed.
    
2. Run `npm install truffle-hdwallet-provider`.
