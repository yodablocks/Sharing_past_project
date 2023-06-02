# Chapter 1: Getting Set Up

In this lesson, we will be covering the theory behind testing **Ethereum** smart contracts, with a focus on **Truffle**, **Mocha**, and **Chai**. You will need an intermediate level of knowledge of **Solidity** and **JavaScript** to help you get the most out of these lessons.

If you are not comfortable with **JavaScript**, consider going through a tutorial elsewhere before starting this lesson.

## Let's Peep Into Our Project

If you followed along with our previous lessons, you should have built a fish-themed game that is largely ready, and your file structure should look like this:

```
├── build
  ├── contracts
      ├── Migrations.json
      ├── CryptoFish.json
      ├── erc721.json
      ├── ownable.json
      ├── safemath.json
      ├── fishattack.json
      ├── fishfactory.json
      ├── fishfeeding.json
      ├── fishhelper.json
      ├── fishownership.json
├── contracts
  ├── Migrations.sol
  ├── CryptoFish.sol
  ├── erc721.sol
  ├── ownable.sol
  ├── safemath.sol
  ├── fishattack.sol
  ├── fishfactory.sol
  ├── fishfeeding.sol
  ├── fishhelper.sol
  ├── fishownership.sol
├── migrations
└── test
. package-lock.json
. truffle-config.js
. truffle.js
```

See the `test` folder? This is where we are going to be putting our tests.

_Truffle_ provides support for tests written in _JavaScript_ and _Solidity_ but, for the scope of this lesson, we are going to keep things simple and stick to _JavaScript_.

# Put it to the test

It is best practice to create a separate test file for each contract and give it the name of the smart contract. This makes managing your tests simpler in the long run, especially as your project grows and changes.

1. In the terminal to the right, run `touch test/CryptoFishs.js`.

