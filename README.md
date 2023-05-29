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

