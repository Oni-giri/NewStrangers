from brownie import *
from brownie import NewStrangers
import json


def main():

    deployer = acct = accounts.load("MyWallet")
    with (open("sft_address.txt", "r")) as f:
        sft_address = f.read()

    sft = NewStrangers.at(sft_address)

    with (open("IdToOwner.json", "r")) as f:
        IdToOwner = json.load(f)

    with (open("ownerToId.json", "r")) as f:
        ownerToId = json.load(f)

    # Add your logic here for determining airdrop
    # We should end up with a dict of addresses, and the amount of SFT to airdrop to each address

    airdrop_data = {
        "0x0000": [{"amount": 100, "token_id": 0}],
    }

    for address in airdrop_data:
        for token in airdrop_data[address]:

            # We check in case we fail to mint the token
            balance = sft.balanceOf(address, token["token_id"])
            if balance == 0:
                sft.mint(address, token["token_id"],
                         token["amount"], "", {'from': deployer})
