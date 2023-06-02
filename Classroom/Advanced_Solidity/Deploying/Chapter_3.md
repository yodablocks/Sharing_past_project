# Chapter 3: Compiling the Source Code

Congratulations! Now that we've put the project structure in place and set up `truffle-hdwallet-provider`, let's compile our contracts.

Why do we need to compile, you ask?

The **_Ethereum Virtual Machine_** can't directly understand Solidity source code as we write it. Thus, we need to run a compiler that will "translate" our smart contract into machine-readable **_bytecode_**. The virtual machine then executes the bytecode, and completes the actions required by our smart contract.

Curious about how does the bytecode look like? Let's take a look:

