# Chapter 1: Intro

By completing Lesson 17, you got a good grasp of the basic functions and concepts of zkSync. Now you're going to modify the Node.js applications you've created so that Alice could pay Bob using ERC20 tokens. In this tutorial, we are going to use USDT, a stablecoin pegged against the U.S. dollar, but your application can use any ERC20 token supported by the protocol.
> 👉🏻For the full list of supported tokens, see the <a href="https://rinkeby.zkscan.io/explorer/tokens" target="_blank">supported tokens on Rinkeby</a> page.

Before we get into the meat and potatoes, let's get yourself some Rinkeby USDT tokens. All you have to do is to follow these steps:

1. Navigate to <a href="https://rinkeby.etherscan.io/token/0x3b00ef435fa4fcff5c209a37d1f3dcff37c705ad" target="_blank">this contract address</a>
2. Click the **Connect to Web3** link, and then select the wallet you want to use. Note that we recommend MetaMask.
2. Select the **Write Contract** tab
3. To get to the end of this lesson, you must mint at least six USDT tokens. Scroll down to the **mint** function, and populate the following fields:
  * **_to**: enter your Rinkeby address
  * **_amount**: enter `6000000` (the USDT token has six decimal places)
4. Select the **Write** button.
5. You'll see a Metamask popup. To approve the transaction, select the **Confirm** button.

Now let's get back to why we're here. The first thing you'll have to do is to configure the `src/alice.js` script to use **_USDT_** instead of **_ETH_** for deposits, transfer, and withdrawals.

## Put it to the test

1. Change the value of the `token` variable to `'USDT'`
2. Change the value of the `amountToDeposit` to `'6.0'`
3. Change the value of the `amountToTransfer` and `amountToWithdraw` variables to `'2.0'`
