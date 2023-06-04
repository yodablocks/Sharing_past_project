# Chapter 1: Using Roles 

In the previous lessons, you've used OpenZeppelin's `Ownable` contract to implement a simple access control mechanism based on the concept of **_ownership_**. Simply put, only the owner was allowed to call the `setLatestEthPrice` function.

Now, to make the oracle more decentralized, we need to implement a system that provides different levels of access: `owner` and `oracle`. The owner should be able to add and remove oracles. In turn, an oracle must be allowed to update the ETH price by calling the `setLatestEthPrice` function.


## Using Roles

Fortunately, OpenZeppelin provides a library called `Roles` that does all the heavy lifting. To you use it, you'll first have to import it using something like the following:

```Solidity
import "openzeppelin-solidity/contracts/access/Roles.sol";
```


Now, that you imported from the `Roles` smart contract, let's see what makes it tick:

```Solidity
pragma solidity ^0.5.0;

/**
 * @title Roles
 * @dev Library for managing addresses assigned to a Role.
 */
library Roles {
    struct Role {
        mapping (address => bool) bearer;
    }

    /**
     * @dev Give an account access to this role.
     */
    function add(Role storage role, address account) internal {
        require(!has(role, account), "Roles: account already has role");
        role.bearer[account] = true;
    }

    /**
     * @dev Remove an account's access to this role.
     */
    function remove(Role storage role, address account) internal {
        require(has(role, account), "Roles: account does not have role");
        role.bearer[account] = false;
    }

    /**
     * @dev Check if an account has this role.
     * @return bool
     */
    function has(Role storage role, address account) internal view returns (bool) {
        require(account != address(0), "Roles: account is the zero address");
        return role.bearer[account];
    }
}
```

Note that `Roles` is a library. For us, this means that we can attach it to the `Roles.Role` data type like so:

```Solidity
using Roles for Roles.Role;
```

Once we do this, the first parameter expected by the `add`, `remove`, and `has` functions (that is `Roles storage role`) is automatically passed, meaning we can use these functions to manage our roles as follows:

```Solidity
oracles.add(_oracle); // Adds `_oracle` to the list of oracles
oracles.remove(_oracle); // Removes `_oracle` from the list of oracles
oracles.has(msg.sender); // Returns `true` if `msg.sender` is an `oracle`
```

## Put It to the Test

1. In the tab to the right, replace the line of code that imports from the `Ownable.sol` file with the line of code that imports from the `Roles.sol` file.
2. Make it so that the contract doesn't inherit from `Ownable` by removing `is Ownable` from the line of code that declares the contract.
3. Attach `Roles` to the `Roles.Role` data type.
4. Declare a `Roles.Role` variable called `owners`. Make it `private`.
5. Similarly, create a `Roles.Role` variable called `oracles`. Don't forget to make it `private` as well.
