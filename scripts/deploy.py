from brownie import *
from brownie import NewStrangers


def main():

    # You URI here
    uri = "test.uri/"
    name = "testSFT"
    symbol = "tstf"

    deployer = accounts[0]
    sft = NewStrangers.deploy(uri, name, symbol, {'from': deployer}, publish_source=True)

    # mint(_to, _tokenId, _amount, _data)
    sft.mint(deployer, 0, 100, "", {'from': deployer})

    print("sft.name()", sft.name())
    print("sft.totalSupply()", sft.totalSupply(0))
    print("sft.balanceOf(deployer)", sft.balanceOf(deployer, 1))
    print("uri", sft.uri(1))
    print("SFT", sft.address)

    with(open("sft_address.txt", "w")) as f:
        f.write(sft.address)
        

