# Chapter 9: Account balances

Great! Now you know how to deposit, transfer, and withdraw assets. What else would your users want to do?

Of course, they would want to see their balance on zkSync.

## Committed and verified balances

<!-- This is a bit hairy... Maybe I should just remove this or simplify it -->

When you transfer assets on zkSync, the operator includes your transaction in a new block and pushes this new block to the zkSync smart contract on Ethereum using a **Commit** transaction. Then, the SNARK proofs for each transaction in the block is and published on Ethereum using a **Verify** transaction. Once the **Verify** transaction is mined on Ethereum, the protocol considers the new state to be final.

Remember that you can receive some tokens and then immediately send those tokens to another user as part of a different transaction? How can that be possible if the protocol waits for the transaction to be mined on Ethereum? The answer is that there are two types of balances on zkSync (**_committed_** and **_verified_**) and you can use the assets in your **committed** balance as you wish.

Just to make things clear:

* The **_committed_** balance  includes all verified and committed transactions
* The **_verified_** balance includes only verified transactions

There are two way in which you can retrieve the balances for an account:

1. Using the `await wallet.getBalance` function as follows:

  ```JavaScript
  const committedETHBalance = await wallet.getBalance('ETH')
  const verifiedETHBalance = await wallet.getBalance('ETH', 'verified')
  ```

2. Retrieving the **account state** which is a JSON object that describes the current state of your account:

  ```JavaScript
  const state = await wallet.getAccountState()
  ```

  If you `console.log` the `state` variable, the output would look similar to the following example:

  ```JSON
  { address: '0xc26f2adeeebbad73f25329ffa12cd3889429b5b6',
    committed:
    { balances: { ETH: '100000000000000000' },
      nonce: 1,
      pubKeyHash: 'sync:de9de11bdad08aa1cdc2beb5b2b7c7f29c10f079' },
    depositing: { balances: {} },
    id: 138,
    verified:
    { balances: { ETH: '100000000000000000' },
      nonce: 1,
      pubKeyHash: 'sync:de9de11bdad08aa1cdc2beb5b2b7c7f29c10f079' } }
  ```

The second method is handier when you want to retrieve balances for multiple assets.

Now, there's something else you should pay attention to before jumping to the part where you write the code: if an account balance is zero, the corresponding JSON field (for example `state.committed.balances.ETH`) will be `undefined`. Trying to `console.log` an `undefined` variable will break your application, so you should gate the lines of code that display the verified and committed balances with an `if/else` statement as follows:

```JavaScript
if (variable) {
  doSomething()
} else {
  doSomethingElse()
}
```

In this example, if `variable` is defined, then the `doSomething` function gets called. Otherwise, if `variable` is `undefined`, then the `doSomethingElse` function gets called.

## Put it to the test

1. Create an `async` function named `displayZkSyncBalance` that takes two parameters: `wallet` and `ethers`
2. The first line of your new function should declare a `const` variable called `state` and set it to `await wallet.getAccountState()`
3. Add an `if/else` block that checks if `state.committed.balances.ETH` is defined.
4. Inside the `if` statement, copy and paste the following line of code:
  ```JavaScript
  console.log(`Commited ETH balance for ${wallet.address()}: ${ethers.utils.formatEther(state.committed.balances.ETH)}`)
  ```
5. Inside the `else` statement, copy and paste the following line of code:
  ```JavaScript
  console.log(`Commited ETH balance for ${wallet.address()}: 0`)
  ```
6. Add a new `if/else` block that checks if `state.verified.balances.ETH` is defined.
7. Inside the second `if` statement, print out to the console the **verified balance**.
8. Inside the second `else` statement, copy and paste the following line of code:
  ```JavaScript
  console.log(`Verified ETH balance for ${wallet.address()}: 0`)
  ```

>Note: This example focuses on simplicity while sacrificing real-world usability. In your application, you would want to place the code that retrieves the balances and displays them in separate functions.
