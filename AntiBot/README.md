<code>+import "path/to/IPAntiBot.sol";</code>

contract MyToken {
<code>+ IPAntiBot public AntiBot;</code>

  constructor(
    string memory name_,
    string memory symbol_,
    uint8 decimals_,
    uint256 totalSupply_,
<code>+   address AntiBot_ </code>
  ) {
    ... omitted for clarity

    // Create an instance of the AntiBot variable from the provided address
    
<code>+   AntiBot = IPAntiBot(AntiBot_);</code>
    // Register the deployer to be the token owner with AntiBot. You can
    // later change the token owner in the AntiBot contract
<code>+   AntiBot.setTokenOwner(msg.sender);</code>
  }

  // Inside ERC20's _transfer function:
  function _transfer(
    address sender,
    address recipient,
    uint256 amount
  ) internal virtual {
    require(sender != address(0), "ERC20: transfer from the zero address");
    require(recipient != address(0), "ERC20: transfer to the zero address");
<code>+   AntiBot.onPreTransferCheck(sender, recipient, amount);</code>
  }
}
