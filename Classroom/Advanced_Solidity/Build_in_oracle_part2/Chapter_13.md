# Chapter 13: Deploy the contracts

In this chapter, we'll briefly walk you through the process of deploying your smart contracts to the Extdev Testnet.

>☞ It's outside the scope of this lesson to delve into details about how Truffle works.

## Generating the Private Keys

Before you deploy the contracts, you must first create two private keys, one for the caller contract and the other one for the oracle.

To do this, we've come up with a simple script. Just create a directory called `scripts` and, inside of that directory, make a file named `gen-key.js`. Then, paste the following content into it:

```JavaScript
const { CryptoUtils } = require('loom-js')
const fs = require('fs')

if (process.argv.length <= 2) {
	console.log("Usage: " + __filename + " <filename>.")
	process.exit(1);
}

const privateKey = CryptoUtils.generatePrivateKey()
const privateKeyString = CryptoUtils.Uint8ArrayToB64(privateKey)

let path = process.argv[2]
fs.writeFileSync(path, privateKeyString)
```

You can now generate the private key for the oracle by entering the `node scripts/gen-key.js oracle/oracle_private_key` command.

Similarly, to generate the private key for the caller contract, run `node scripts/gen-key.js caller/caller_private_key`.

## Configuring Truffle

Next, you must let Truffle know how to deploy on Extdev Testnet. Because the oracle and the caller contract use different private keys, the easiest way is to create separate configurations.

* For the oracle, create a file called `oracle/truffle-config.js` with the following content:

  ```JavaScript
  const LoomTruffleProvider = require('loom-truffle-provider')

  const path = require('path')
  const fs = require('fs')

  module.exports = {
    networks: {
      extdev: {
        provider: function () {
          const privateKey = fs.readFileSync(path.join(__dirname, 'oracle_private_key'), 'utf-8')
          const chainId = 'extdev-plasma-us1'
          const writeUrl = 'wss://extdev-plasma-us1.dappchains.com/websocket'
          const readUrl = 'wss://extdev-plasma-us1.dappchains.com/queryws'
          return new LoomTruffleProvider(chainId, writeUrl, readUrl, privateKey)
        },
        network_id: '9545242630824'
      }
    },
    compilers: {
      solc: {
        version: '0.5.0'
      }
    }
  }
  ```

* For the caller contract, create a file named `caller/truffle-config.js` and paste the above snippet into it. Then, edit this line:

  ```JavaScript
  const privateKey = fs.readFileSync(path.join(__dirname, 'oracle_private_key'), 'utf-8')`
  ```

  to:

  ```JavaScript
  const privateKey = fs.readFileSync(path.join(__dirname, 'caller_private_key'), 'utf-8')`
  ```

## Create the migration files

To deploy the oracle contract, you must create a file called the `./oracle/migrations/2_eth_price_oracle.js` with the following content:


```JavaScript
const EthPriceOracle = artifacts.require('EthPriceOracle')

module.exports = function (deployer) {
  deployer.deploy(EthPriceOracle)
}
```

Similarly, to deploy the caller contract, you must create a file called `./caller/migrations/02_caller_contract.js` with the following content:

```JavaScript
const CallerContract = artifacts.require('CallerContract')

module.exports = function (deployer) {
  deployer.deploy(CallerContract)
}
```

## Updating the package.json file

At this point, you're ready to deploy your contracts. But that'll require you to enter the following commands:

```JavaScript
cd oracle && npx truffle migrate --network extdev --reset -all && cd ..
```

followed by:

```JavaScript
cd caller && npx truffle migrate --network extdev --reset -all && cd ..
```


Well, I'm not a big fan of typing this every time I want to deploy the contracts. Let's make it easier by modifying the `scripts` section of the `package.json` file to this:

```json
"scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "deploy:oracle": "cd oracle && npx truffle migrate --network extdev --reset -all && cd ..",
    "deploy:caller": "cd caller && npx truffle migrate --network extdev --reset -all && cd ..",
    "deploy:all": "npm run deploy:oracle && npm run deploy:caller"
  },
```

## Put It to the test

1. Now you can deploy the smart contracts with one command! Type `npm run deploy:all` in the box to the right, and then press `Enter`.

And that's it, you've just deployed both contracts. So much easier than you've expected, isn’t it?
