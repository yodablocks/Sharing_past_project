# Chapter 2: Work with tokens

As you've seen in the previous chapter, the zkSync protocol supports quite a few tokens, and each token has its own characteristics. For us, the most relevant are the following:

* The token's symbol (`ETH`, `USDT`, etc)
* The number of decimals (`ETH` has 18 decimals, `USDT` has six decimals)

The number of decimals is something you must pay special attention to because, if you want to write an application that supports multiple tokens, the values for depositing, transferring, and withdrawing assets need a bit of massaging before you send them to the zkSync protocol.

In the previous lesson, you've used the `ethers.utils.formatEther` and `ethers.utils.parseEther` functions, but they won't be helpful now that your application must deal with tokens that have a different number of decimals.

## The TokenSet class

Luckily, zkSync provides a class named `TokenSet` that does all the heavy lifting for you.

To obtain an instance of the `TokenSet` class, you'll have to use something like the following:

```JavaScript
const tokenSet = zkSyncProvider.tokenSet
```

Next, you can call the `parseToken` function to convert a value from a human-readable format to `BigNumber`:

```JavaScript
const amountAsBigNumber = tokenSet.parseToken(token, amountInHumanReadableForm)
```

If you want to convert a value from `BigNumber` to a human-readable form, you should then call the `formatToken` function:

```JavaScript
const amountInHumanReadableForm = tokenSet.formatToken(token, amountAsBigNumber)
```

## Retrieve Alice's USDT balance on Ethereum

Once the `alice.js` application instantiates an Ethereum wallet, then it does the following:

1. Retrieves Alice's ETH  balance on Ethereum
2. Calls the `ethers.utils.formatEther` to format the `aliceInitialRinkebyBalance` variable to a human-readable form
3. Displays Alice's ETH balance

To refresh your memory, take a look at the next snippet:

```JavaScript
const aliceInitialRinkebyBalance = await aliceRinkebyWallet.getBalance()
console.log(`Alice's initial balance on Rinkeby is: ${ethers.utils.formatEther(aliceInitialRinkebyBalance)}`)
```

Obviously, now you'll want to retrieve Alice's USDT balance instead. To do this, you should call the `getEthereumBalance` of the `zksync.Wallet` object. The function takes one parameter: the name of the token for which it should retrieve the balance.

Example:

```JavaScript
const yourUSDTBalance = await yourZkSyncWallet.getEthereumBalance(token)
```

## Put it to the test

1. Delete the line of code that retrieves Alice's initial ETH  balance on Rinkeby.
2. Cut the line of code that uses `ethers.utils.formatEther` to format Alice's balance to a human-readable form and then display it. Don't delete this line, you'll use it in the last step.
3. Obtain an instance of the `TokenSet` class and store the result in a `const` variable named `tokenSet`
4. Retrieve Alice's initial USDT balance on Rinkeby by calling the `getEthereumBalance` function of the `aliceZkSyncWallet` object, passing it the `token` variable as a parameter, and storing the result in a `const` variable named `aliceInitialRinkebyBalance`. This is an asynchronous function, don't forget to `await` for the promise to resolve!
5. Display Alice's initial USDT balance on Rinkeby by pasting the line you've copied in step 2. Replace `ethers.utils.formatEther` with `tokenSet.formatToken`. The function takes two parameters: `token` and `aliceInitialRinkebyBalance`
