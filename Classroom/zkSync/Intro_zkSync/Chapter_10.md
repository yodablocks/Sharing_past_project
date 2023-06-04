# Chapter 10: The shopkeeper - Talking to the blockchain

Great! Writing the functions that interact with zkSync was the difficult part — now implementing the Node.JS applications for the shopkeeper (Bob) and the customer (Alice) will be straightforward. But before you do that, note that we've added a `module.exports` object to the `utils.js` file. This specifies which functions and variables Node.js should export from this file.

## Top-level await

All the functions you added to the `utils.js` file are asynchronous, but Node.js only allows you to place the `await` operator inside an `async` function. A common solution is to wrap your code in an **immediately invoked async function**.

If this sounds complicated, then let's take an example:

```JavaScript
(async () => {
  await myAsyncFunction()
})()

```

Do you see? That wasn't complicated at all.

Now let's put what you've learned together and start fleshing out the shopkeeper application.

## Put it to the test

We've created a new file for you called `bob.js`, added an immediately invoked function, and imported the following modules: `ethers`, `zksync`, `./utils`.

1. To connect to zkSync, you must create a zkSync provider by calling the `utils.getZkSyncProvider` function. It's an `async` function that takes two parameters: `zksync`, `process.env.NETWORK_NAME`. Store the result in a `const` variable named `zkSyncProvider`.
>Note: The `process.env` property returns an object that represents your environment. Before you run this Node.js application, you must set the value of the `NETWORK_NAME` environment variable as follows:
  ```shell
    export NETWORK_NAME=rinkeby
  ```

2. The code for creating a Rinkeby provider is almost identical. Just call a function named `utils.getEthereumProvider` and store the result in a `const` variable named `ethersProvider`. The function takes the following two parameters: `ethers`, and `process.env.NETWORK_NAME`.
