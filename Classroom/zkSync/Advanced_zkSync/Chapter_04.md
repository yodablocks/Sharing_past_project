# Chapter 4: Approve ERC20 token transfers

Awesome! Now, there's one last thing left before we move to the `utils.js` file.

Your application will use the `tokenSet` object to convert values between `BigNumber` and a human-readable format (and vice versa), so the functions in the `utils.js` module will need to be updated to take a `TokenSet` instance as a parameter instead of `ethers`.


## Put it to the test

1. In the tab to the right, update the lines of code that call the following functions:

  * `utils.depositToZkSync`. This function should take the following parameters:
    * `aliceZkSyncWallet`
    * `token`
    * `amountToDeposit`
    * `tokenSet`
  * `utils.displayZkSyncBalance`. This function should take the following parameters:
    * `aliceZkSyncWallet`
    * `tokenSet`
  * `utils.getFee`. This function should take the following parameters:
    * `'Transfer'` or `'Withdraw'`
    * `aliceRinkebyWallet.address`
    * `token`
    * `zkSyncProvider`
    * `tokenSet`
  * `utils.transfer`. This function should take the following parameters:
    * `aliceZkSyncWallet`
    * `process.env.BOB_ADDRESS`
    * `amountToTransfer`
    * `transferFee`
    * `token`
    * `zksync`
    * `tokenSet`
  * `utils.withdrawToEthereum`. This function should take the following parameters:
    * `aliceZkSyncWallet`
    * `amountToWithdraw`
    * `withdrawalFee`
    * `token`
    * `zksync`
    * `tokenSet`

> 👉🏻 Be careful, the `utils.getFee` and `utils.displayZkSyncBalance` functions are invoked twice!
