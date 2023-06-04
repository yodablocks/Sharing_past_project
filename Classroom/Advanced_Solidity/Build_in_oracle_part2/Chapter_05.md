# Chapter 5: Processing the Queue

In the previous chapter, we've created an empty shell for the `processQueue` function. Let's now focus on filling it in.

* The first thing your function should do is to retrieve the first element from the `pendingRequest` array. Of course, once retrieved, the element should also be removed from the array. In JavaScript, you can do this by calling the `shift` method which returns the first element of the array, removes the element from the array, and changes the length of the array. Continuing our example from the second chapter, here's how `shift` works:

  ```JavaScript
  let numbers = [ { 1: 'one' }, { 2: 'two' }, { 3: 'three' } ]
  const item = numbers.shift()
  console.log(item)
  ```

  This prints `{ '1': 'one' }`.

* Then, you'll have to call the `processRequest` function. I see you raising your eyebrow and asking: what does this function actually do? The simple answer is that it... processes the request. The detailed answer would be that it fetches the ETH price, and then calls the oracle smart contract. Don't worry about it right now, you'll write it in the next chapters.

* Lastly, you'll have to increment the `processedRequests` variable.

## Put It to the Test

1. Inside of the `while` loop, call `shift` to remove the first element from the `pendingRequests` array. Store it in a `const` called `req`.
2. Execute the `processRequest` function. It takes the following arguments:

  * `oracleContract` and `ownerAddress`, coming from the function's arguments
  * `id` and `callerAddress`, properties of the `req` object.
  >Note: In JavaScript, there are two ways in which you can access the properties of an object: using the **dot notation** (`myObject.myProperty`) or the **bracket notation** (`myObject['myProperty']`). I find the dot notation more concise, let's use it.

  This is an `async` function. Use `await` when you call it!

3. Before you wrap up this function, use `++` to increment the `processedRequests` variable. Otherwise, your function will end up running in an infinite loop.
