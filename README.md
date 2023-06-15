# New Strangers

This repo contains a script to extract the current ownership of the NFT project ["Strangers"](https://etherscan.io/address/0x36d079c175026a046da91e1b3912a4345812340d).

To setup everything, you'll need to have Python3 available.

Run the following in the terminal:

```bash
python3 virtualenv venv
pip install eth-brownie
brownie networks add "Ethereum Mainnet" mainnet host=[your RPC url] 
```

You can now run `brownie` and you should see the options in the terminal.

To make a snapshot of ownerships:

```bash
brownie run scripts/snapshot.py
```

This will create two JSON files : `IdToOwner.json`and `OwnerToId.json`.

To deploy the contracts, you'll need to add your private key to the brownie config file. You can do this by running `brownie accounts new [account name]` and entering your private key when prompted.

You can then add your etherscan API key using `export ETHERSCAN_TOKEN=[key]`

Now that you have the snapshot, you can run the script to deploy the contract :
`brownie run scripts/deploy.py --network mainnet -i` - if you want to deploy the contract on mainnet.

`brownie run scripts/deploy.py --network rinkeby -i` - if you want to deploy the contract on rinkeby.

`brownie run scripts/deploy.py -i` - if you want to test the deployment on a local fork.

You'll need to add some logic to the `airdrop.py` script to actually send the tokens to the addresses you want to airdrop to. You can use the `mint` function of the contract to do that in a gas-efficient way.

```bash

```

```bash

```

