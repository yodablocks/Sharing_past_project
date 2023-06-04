# Chapter 10: Returning multiple values in JavaScript

The logic for the `retrieveLatestEthPrice` is trivial to implement and we won't be spending time explaining it. We've just placed the code below the `getOracleContract` function. Be sure to give it a read so you understand how it works.

Now, the good news is that you're close to wrapping up the oracle. But still, there a few small things left for you to do. For example, let's look into what happens when you start the oracle.

So, every time the oracle starts, it has to:
* connect to Extdev TestNet by calling the `common.loadAccount` function
* instantiate the oracle contract
* start listening for events

To keep the code clean, you'd want to put all this stuff inside of a function. This function should return a bunch of values needed by other functions:

* `client` (an object the app uses to interact with the Extedev Testnet),
* An instance of the oracle contract, and
* `ownerAddress` (used in the `setLatestEthPrice` to specify the address that sends the transaction).

Now, this is a bit of a challenge because, in JavaScript, functions can't return multiple values. But this doesn't prevent a function from returning... an object or an array, right?

Correct. So this is how you can get a similar result in JavaScript by using an object:

```JavaScript
function myAwesomeFunction () {
  const one = '1'
  const two = '2'
  return { one, two }
}
```

Then, the code that calls this function must unpack the values:

```JavaScript
const { one, two } = myAwesomeFunction()
```

## Put It to the Test

We created an empty `init` function for you. Let's put the knowledge you acquired in this lesson to work, and fill in the body of the function.

1. The first line of code should run the `common.loadAccount` function. It takes one argument: `PRIVATE_KEY_FILE_NAME`. This function returns an object containing three properties: `ownerAddress`, `web3js`, and `client`. Unpack them. If you didn't follow that, just take a look at the example above where we unpacked `one` and `two`. Your solution should be very similar.

2. Let's instantiate the oracle contract by calling the `getOracleContract` function. It takes one parameter (`web3js`) and returns a promise. You must `await` for the promise to resolve and store the result into a `const` called `oracleContract`.

3. Run the `filterEvents` function passing it `oracleContract` and `web3js` as arguments.

4. The last line of your function should form and `return` an object containing the following properties: `oracleContract`, `ownerAddress`, `client`.
