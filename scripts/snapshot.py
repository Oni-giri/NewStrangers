from brownie import *
import json


def main():

    nft = Contract.from_explorer("0x36d079c175026a046da91e1b3912a4345812340d")

    ownerToId = {}
    IdToOwner = {}
    for i in range(0, nft.totalSupply()):
        owner  = nft.ownerOf(i+1)

        if owner in ownerToId and len(ownerToId[owner]) > 0:
            ownerToId[owner].append(i+1)
        else:
            ownerToId[owner] = [i+1]

        IdToOwner[i+1] = owner
        print(i+1, owner)
    
    with open('ownerToId.json', 'w') as fp:
        json.dump(ownerToId, fp)
        fp.close()
    
    with open('IdToOwner.json', 'w') as fp:
        json.dump(IdToOwner, fp)
        fp.close()
    
