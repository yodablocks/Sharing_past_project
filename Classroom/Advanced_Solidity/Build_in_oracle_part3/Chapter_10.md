# Chapter 10: Using SafeMath

We're close to being done with the decentralized oracle! Before we conclude, let's do the following:

* Delete the `id` key from the `requestIdToResponse`.
* Update `setLatestEthPrice` function so that it calls `callerContractInstance.callback` with `computedEthPrice`.
* The first argument passed to `SetLatestEthPriceEvent` should be `computedEthPrice`


## Put It to the Test

1. Go ahead and delete the `_id` key from the `requestIdToResponse` map.
2. Go ahead and update the last two function calls (`callerContractInstance.callback` and `SetLatestEthPriceEvent`), replacing `_ethPrice` with `computedEthPrice`.
