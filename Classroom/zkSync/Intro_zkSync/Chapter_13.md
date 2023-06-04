# Chapter 13: Register an account

Having coded the shopkeeper application, the next thing on your list should be the application Alice will use.

Take a look at the screen to the right. To get everything ready for you, we've:

* Created a new JavaScript file called `alice.js`
* Imported a few prerequisites
* Defined the following `const` variables:
  ```JavaScript
  const token = 'ETH'
  const amountToDeposit = '0.05'
  const amountToTransfer = '0.02'
  const amountToWithdraw = '0.002'
  ```
* Filled in the code that connects your app to Rinkeby and zkSync.

Here's what we'll implement in the next few chapters:

1. Alice will deposit some ETH to her zkSync account.
2. Alice will register her public key with zkSync so she can transfer assets via zkSync.
3. Alice will make a payment to Bob via zkSync.
4. Alice will withdraw her remaining ETH from zkSync to Ethereum.

Let's take a stab at it.

## Put it to the test

1. Add a line of code that calls the `utils.depositToZkSync` function. It's an `async` function that takes the following parameters: `aliceZkSyncWallet`, `token`, `amountToDeposit`, `ethers`.
2. To display Alice's balance on zkSync, invoke the `await utils.displayZkSyncBalance` function, passing it `aliceZkSyncWallet` and `ethers` as parameters. Don't forget it's an `async` function!
3. Alice won't be able to make a payment unless she gets her public key registered on zkSync. Let's do that by calling the `utils.registerAccount` function, and passing it `aliceZkSyncWallet` as a parameter. As with all functions that interact with the blockchain, it returns a promise. You already know how to call this function!🤓
