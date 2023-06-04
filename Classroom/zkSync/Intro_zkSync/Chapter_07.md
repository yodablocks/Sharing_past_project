# Chapter 7: Transfer fees

On zkSync, operations are cheap but they're not free. In this chapter, we're going to continue by teaching you how you can calculate the fee associated with each transaction.

As the protocol performs the computation and stores the state off-chain, the fees users must pay are comprised of two separated components:

* **off-chain** fee, representing the cost of computation and storage. This component is **invariable**
* **on-chain** fee, representing the cost of verifying the SNARK on Ethereum. This cost is amortized across all transactions in a block, and it's variable because it depends on the price of gas.


Here's an example of computing the fee for a specific transaction:

```JavaScript
const feeInWei = await zkSyncProvider.getTransactionFee(transactionType, address, token)
```

In this example, the `getTransactionFee` function takes three parameters:

  * **transactionType**: specifies whether this is a **"Withdraw"** or **"Transfer"**
  * **address**: represents the address of the recipient
  * **token**: specifies the type of token you want to transfer (e.g. **"ETH"**)

The `getTransactionFee` returns a promise which resolves to an object with the following structure:

```JavaScript
export interface Fee {
    // Operation type (amount of chunks in operation differs and impacts the total fee).
    feeType: "Withdraw" | "Transfer" | "TransferToNew",
    // Amount of gas used by transaction
    gasTxAmount: utils.BigNumber,
    // Gas price (in wei)
    gasPriceWei: utils.BigNumber,
    // Ethereum gas part of fee (in wei)
    gasFee: utils.BigNumber,
    // Zero-knowledge proof part of fee (in wei)
    zkpFee: utils.BigNumber,
    // Total fee amount (in wei)
    // This value represents the summarized fee components, and it should be used as a fee
    // for the actual operation.
    totalFee: utils.BigNumber,
}
```

Now you can do the math and add up all components of the fee, or just use `totalFee`.

Which one do you choose?

There's no need to answer this question, I probably already know the answer.😉

But, as with transfers, this function expresses all values in `wei`.
If you want to present the fee to your users, you'd better convert it to a human-readable form by:

* converting it from `BigNumber` to string
* calling the `ethers.utils.formatEther` function

**Example:**

```JavaScript
const fee = ethers.utils.formatEther(feeInWei.toString())
```

That's how easy it is to calculate the fee!

## Put it to the test

1. Declare an `async` function named `getFee`. It takes five parameters: `transactionType`, `address`, `token`, `zkSyncProvider`, `ethers`.

2. Declare a `const` named `feeInWei` and set it to `await zkSyncProvider.getTransactionFee`. Don't forget that this function takes the following parameters: `transactionType`, `address`, `token`.

3. Return the fee in a human-readable form by converting `feeInWei.totalFee` to a `string` and then passing this value as an argument to the `ethers.utils.formatEther`. Too easy? Do this in **one line of code** to keep things clean.

> The solution should be 4 lines of code (including the closing `}` of the function).

And there you go! That's the final step of this chapter that returns the fee.
