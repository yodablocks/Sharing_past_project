# Chapter 14: Make a payment on zkSync

Having registered her public key on zkSync, Alice wants to make a payment to Bob. Are you ready to help her out?

First, you'll have to retrieve the transfer fee by calling the `utils.getFee` function.

Second, just call the `utils.transfer` function.

>Note: For convenience, we've stored Bob's address in an environment variable. Before you run the `bob.js` script, you'll have set it as follows: `export BOB_ADDRESS=<BOB_ACTUAL_ADDRESS>


## Put it to the test

1. To retrieve the transfer fee, call the `utils.getFee` function, `await` for the promise to resolve, and store the result in a `const` variable named `transferFee`. The `utils.getFee` function takes the following parameters:

  * The 'Transfer' string (the type of transaction)
  * `aliceRinkebyWallet.address` (Alice's address on Rinkeby)
  * `token` (we've set this to `ETH` on line 5)
  * `zkSyncProvider`
  * `ethers`

2. Run the `utils.transfer` function. It takes the following parameters:

  * `aliceZkSyncWallet`
  * `process.env.BOB_ADDRESS`
  * `amountToTransfer`
  * `transferFee`
  * `token`
  * `zksync`
  * `ethers`

  Don't forget that it's an `async` function!
