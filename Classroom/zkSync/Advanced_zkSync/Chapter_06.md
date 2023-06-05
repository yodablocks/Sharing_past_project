# Chapter 6: Update the displayZkSyncBalance function

Awesome, you've updated the `depositToZkSync` function! Take that as a sign that you've warmed up. And the good news is that there's more where that came from.

But before we begin, just a word of warning: updating the `displayZkSyncBalance` function is going to put your JavaScript knowledge to the test.

As a quick refresher, the first line of this function retrieves your account state and stores in a `const` variable named `state`:

```JavaScript
const state = await wallet.getAccountState()
```

Now, if you `console.log` the `state` variable, you'll see something similar to the following output:

```JSON
{ address: '0xc26f2adeeebbad73f25329ffa12cd3889429b5b6',
  committed:
   { balances: { ETH: '99891300000000000', USDT: '241896200' },
     nonce: 5,
     pubKeyHash: 'sync:de9de11bdad08aa1cdc2beb5b2b7c7f29c10f079' },
  depositing: { balances: {} },
  id: 83,
  verified:
   { balances: { ETH: '99891300000000000', USDT: '235896200' },
     nonce: 5,
     pubKeyHash: 'sync:de9de11bdad08aa1cdc2beb5b2b7c7f29c10f079' }
}
```

Do you know how you can parse this object and print only the ETH and USDT balances?

## The for...in statement

To display the ETH and USDT balances, you'll use a `for...in` statement that iterates over all enumerable properties of an object.

Let's look at a simple example:

```JavaScript
const myBalances = { usdtBalance: 1, ethBalance: 2};

for (const property in balances) {
  console.log(`${property}: ${object[property]}`);
}
```

If you run this snippet, you'll see the following output printed out to the console:

```
usdtBalance: 1
ethBalance: 2
```

Enough theory, let's write some code!

## Put it to the test

We've gone ahead removed most of the code in the `displayZkSyncBalance` function. Note that we didn't have to remove all these lines of code, but it's a lot easier to explain the changes this way.

1. Let's begin by replacing the last parameter that the `displayZkSyncBalance` function takes (`ethers`) with `tokenSet`
2. Declare a `const` variable named `committedBalances` and assign it to `state.committed.balances`
3. Declare a `const` variable named `verifiedBalances` and assign it to `state.verified.balances`
4. Write a `for...in` loop that uses a `const` variable named `property` to iterate over the `committedBalances` variable. Then, inside this `for...in` loop, paste the following line of code that displays the committed balances:
  ```JavaScript
  console.log(`Committed ${property} balance for ${wallet.address()}: ${tokenSet.formatToken(property, committedBalances[property])}`)
  ```
5. Write a `for...in` loop that uses a `const` variable named `property` to iterate over the `verifiedBalances` variable. Then, inside this `for...in` loop, paste the following line of code that displays the verified balances:
  ```JavaScript
  console.log(`Verified ${property} balance for ${wallet.address()}: ${tokenSet.formatToken(property, verifiedBalances[property])}`)
  ```
