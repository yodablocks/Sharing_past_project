# Chapter 6: Keeping Track of Responses

In this chapter, you're going to start updating the `setLatestEthPrice` function to make the contract work in a more decentralized manner.

With more oracles added, your contract expects more than one response for each request. Thus, the way you're keeping track of responses (that is by adding them to the `pendingRequests` mapping) has to change.

So how should you go about it?

To keep track of everything, for each response, you'll want to store the following:

* `oracleAddress`
* `callerAddress`
* `ethPrice`

Then, you'll want to associate these variables with the identifier of the request.

And one more thing. It'd be nice if you could do this without throwing away all your work and starting over.

To accomplish this, you're going to use a `mapping` that'll associate each request id to an array of `struct`s containing `oracleAddress`, `callerAddress`, and `ethPrice` variables.

>Note: In Solidity, you can define a `struct` using something like the following:

  ```Solidity
  struct MyStruct {
    address anAddress;
    uint256 aNumber;
  }
  ```

  Then, you can instantiate `MyStruct` like so:

  ```Solidity
  MyStruct memory myStructInstance; // declare the struct
  myStructInstance = MyStruct(msg.sender, 200); // initialize it
  ```

  ☞ Did you notice the `memory` keyword? **_Starting with Solidity 5.0, it is mandatory to specify the data location for every reference type!_**

  Of course, you can change the value of an object's member using an assignment statement, the same way you'd assign a value to any other plain variable. Just keep in mind that, in Solidity, we refer to structs and their members are using the dot notation:

  ```Solidity
  myStructInstance.anAddress = otherAddress
  ```

## Put It to the Test

We've gone ahead and removed the `onlyOwner` modifier from the `setLatestEthPrice` function definition, and added a `require` statement that makes sure `oracles.has(msg.sender)` (once again, please excuse the grammar!). We've also added the line of code that defines the `requestIdToResponse` mapping. Make sure you browse through the code before moving on.

1. Let's start by defining a `struct` named `Response` with the following properties inside of it: `oracleAddress` (an `address`), `callerAddress` (an `address`), and `ethPrice` (a `uint256`).
2. Now let's move to the `setLatestEthPrice`. Declare a `Response` variable called `resp`. It should be stored in `memory`.
3. Initialize `resp` with the following values `msg.sender`, `_callerAddress`, and `_ethPrice`.
4. Push `resp` to the array stored at `requestIdToResponse[_id]`.
