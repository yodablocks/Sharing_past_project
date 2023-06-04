# Chapter 1: Settings Things Up

Before we begin, let's be clear: this is an intermediate lesson, and it requires a bit of **_JavaScript_** and **_Solidity_** knowledge.

If you're new to Solidity, it's highly recommended that you go over the first lessons before starting this one.

If you are not comfortable with **JavaScript**, consider going through a tutorial elsewhere before starting this lesson.

---

Let's imagine you're developing a DeFi dapp and want to enable your users to withdraw a specific amount of USD-equivalent ETH. To accomplish this, your smart contract (referred to as the "caller contract" for simplicity) needs to determine the value of one Ether.

Here's the catch: while a JavaScript application can easily retrieve this information by making requests to the Binance public API or any other price feed service, a smart contract lacks direct access to external data. Instead, it relies on an **_oracle_** to fetch the required data.

Initially, this might seem like a daunting task 🤯. However, by breaking it down into manageable steps, we can guide you through the process smoothly.

We understand that visuals can sometimes be more helpful than words alone, so here's a straightforward diagram illustrating how this process operates:

<img src="https://blog.irismetrics.xyz/wp-content/uploads/2023/06/EthPriceOracleOverview.png" alt="Eth Price Oracle Overview" width="469">

Let this sink in before you read on.

For now, let's initialize your new project.

## Put It to the Test

Fire up a terminal window and move into your projects directory. Then, create a directory called `EthPriceOracle` and `cd` into it.

1. In the box to the right, initialize your new project by running the `npm init -y` command.

2. Next, let's install the following dependencies: `truffle`, `openzeppelin-solidity`, `loom-js`, `loom-truffle-provider`, `bn.js`, and `axios`.

  >Note:  You can install multiple packages by running something like the following:

  ```bash
  npm i <package-a> <package-b> <package-c>
  ```

  Why do you need all these packages you ask? Read on and things will become clearer.

  You'll be using Truffle to compile and deploy your smart contracts to Loom Testnet so we've gone ahead and created two bare-bones Truffle projects:

  * The oracle will live in the `oracle` directory:

  ```bash
  mkdir oracle && cd oracle && npx truffle init && cd ..
  ```

  ```
  ✔ Preparing to download box
  ✔ Downloading
  ✔ cleaning up temporary files
  ✔ Setting up box
  ```

   * The caller contract will live in the `caller` directory:

  ```bash
  mkdir caller && cd caller && npx truffle init && cd ..
  ```

  ```
  ✔ Preparing to download box
  ✔ Downloading
  ✔ cleaning up temporary files
  ✔ Setting up box
  ```

  We trust you to do the same and, if everything goes well, your directory structure should look something like the following:

  ```bash
  tree -L 2 -I node_modules
  ```

  ```
  .
  ├── caller
  │   ├── contracts
  │   ├── migrations
  │   ├── test
  │   └── truffle-config.js
  ├── oracle
  │   ├── contracts
  │   ├── migrations
  │   ├── test
  │   └── truffle-config.js
  └── package.json
  ```

  >Note: Learning how to use Truffle is beyond the scope of this lesson.
