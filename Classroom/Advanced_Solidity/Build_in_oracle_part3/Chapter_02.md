# Chapter 2: Using Constructor to Set the Owner

Now that your contract doesn't inherit from `Ownable`, you must find a way to specify its owner. You'll do this by adding a `constructor`. This is a special function that's **_executed only once_**, when a contract gets deployed.

Here's an example of using a constructor:

```Solidity
contract MyAwesomeContract {
  constructor (address _owner) public {
    // Do something
  }
```

To make this work, your constructor should take a parameter - the owner's address. So you must revisit the migration file and edit the line that deploys the smart contract to something like the following:

```JavaScript
deployer.deploy(EthPriceOracle, '0xb090d88a3e55906de49d76b66bf4fe70b9d6d708')
```

Next, the code inside the constructor must add the owner (which comes from the function's arguments) to the list of owners:

```Solidity
owners.add(_owner);
```

## Put It to the Test

1. Define a `constructor` for the `EthPriceOracle` contract. It takes one argument, `_owner` (an `address`). Make it public.
2. The constructor body should add `_owner` to the list of `owners`.
