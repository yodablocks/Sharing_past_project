# Chapter 9: Working with Numbers in Ethereum and JavaScript

Remember we've mentioned that data needs a bit of massaging before it's sent to the oracle contract. Let's look into why.

The Ethereum Virtual Machine doesn't support floating-point numbers, meaning that **_divisions truncate the decimals_**. The workaround is to simply multiply the numbers in your front-end by `10**n`. The Binance API returns eight decimals numbers and we'll also multiply this by `10**10`. Why did we choose `10**10`? There's a reason: one ether is 10**18 wei. This way, we'll be sure that no money will be lost.

But there's more to it. The `Number` type in JavaScript is "double-precision 64-bit binary format IEEE 754 value" which supports only 16 decimals...

Luckily, there's a small library called `BN.js` that'll help you overcome these issues.

> ☞ For the above reasons, it's recommended that you always use `BN.js` when dealing with numbers.

Now, the Binance API returns something like `169.87000000`.

Let's see how you can convert this to `BN`.

First, you'll have to get rid of the decimal separator (the dot). Since JavaScript is a dynamically typed language (that's a fancy way of saying that the interpreter analyzes the values of the variables at runtime and, based on the values, it assigns them a type), the easiest way to do this is...

```JavaScript
aNumber = aNumber.replace('.', '')
```

Continuing with this example, converting `aNumber` to `BN` would look something like this:

```JavaScript
const aNumber = new BN(aNumber, 10)
```

>Note: The second argument represents the base. Make sure it's always specified.

We've gone ahead and filled in almost all the code that goes to the `setLatestEthPrice` function. Here's what's left for you to do.

## Put It to the test

1. The function takes a parameter called `ethPrice` which is the actual value returned by the Binance API. Let's remove the `.` by running the `replace` function on it.
2. Create a `const` called `multiplier`. Initialize it with `10**10` typecasted as a `BN`. This should be almost similar to the `aNumber` example above.
