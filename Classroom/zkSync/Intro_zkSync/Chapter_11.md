# Chapter 11: The shopkeeper - Wallets and private keys

Now, the next thing you should focus on is to instantiate Bob's zkSync wallet.

Do you recall what you've learned in Chapter 3? Every zkSync wallet has an Ethereum address associated with it. Thus, you should first instantiate a Rinkeby wallet for Bob.

## Create a new Rinkeby wallet

Ethereum uses a private key to make sure that you signed a specific transaction, and you need to provide this private key as a parameter when you instantiate a wallet. As long as no one else knows your private key, there's no risk that someone could submit a fake transaction on your behalf. Creating a new wallet for Bob means that the Node.js application you're building will be able to sign transactions on Bob's behalf using his private key.

Since revealing a private key may put your money at risk it's time to get more serious about security. Thus we'll read this private key from an environment variable called `BOB_PRIVATE_KEY`.

That said, you can create a new Ethereum wallet as follows:

```JavaScript
const rinkebyWallet = new ethers.Wallet(process.env.YOUR_PRIVATE_KEY, ethersProvider)
```

The `ethers.Wallet` object provides a few useful helper functions and properties. Let's take a closer look.

### Display Bob's address

Once you've created a Rinkeby wallet, you can display Bob's address with a single line of code:

```JavaScript
console.log(`Bob's Rinkeby address is: ${rinkebyWallet.address}`)
```

Um, to retrieve the address from the zkSync wallet you gotta do `wallet.address()`, but for ethers, you gotta do `wallet.address`? That's unfortunate.

### Display Bob's balance

It would be nice if you could display Bob's initial balance on Rinkeby. Luckily, this is pretty straightforward also:

```JavaScript
console.log(`Bob's initial balance on Rinkeby is: ${ethers.utils.formatEther(await rinkebyWallet.getBalance())}`)
```

## Put it to the test

1. Create a new Rinkeby wallet for Bob. Make a copy of the example above, adjusting the following:
  * The first parameter should be Bob's private key, you can grab it from the `process.env.BOB_PRIVATE_KEY` environment variable
  * The name of the `const` variable used to store the wallet should be `bobRinkebyWallet`.
2. Show Bob's address on Rinkeby and his initial balance.
3. Before we wrap up this chapter, let's create a zkSync wallet for Bob. Declare a `const` variable named `bobZkSyncWallet`, and set it to `await utils.initAccount(bobRinkebyWallet, zkSyncProvider, zksync)`
