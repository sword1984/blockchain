"""
@author: Sword
@email: 173963781@qq.com
@site:
@file: example.py
@time: 4/8/2022 2:14 PM
"""

from hdwallet import BIP44HDWallet
from hdwallet.cryptocurrencies import EthereumMainnet
from hdwallet.derivations import BIP44Derivation
from hdwallet.utils import generate_mnemonic
from typing import Optional


def main(MNEMONIC):
    # Generate english mnemonic words
    # MNEMONIC: str = generate_mnemonic(language="english", strength=128)
    # MNEMONIC: str = 'stage derive easy spend will purpose iron thunder love select kidney inch'
    # Secret passphrase/password for mnemonic
    PASSPHRASE: Optional[str] = None  # "meherett"

    # Initialize Ethereum mainnet BIP44HDWallet
    bip44_hdwallet: BIP44HDWallet = BIP44HDWallet(cryptocurrency=EthereumMainnet)
    # Get Ethereum BIP44HDWallet from mnemonic
    bip44_hdwallet.from_mnemonic(
        mnemonic=MNEMONIC, language="english", passphrase=PASSPHRASE
    )
    # Clean default BIP44 derivation indexes/paths
    bip44_hdwallet.clean_derivation()

    # Get Ethereum BIP44HDWallet information's from address index
    for address_index in range(1):
        # Derivation from Ethereum BIP44 derivation path
        bip44_derivation: BIP44Derivation = BIP44Derivation(
            cryptocurrency=EthereumMainnet, account=0, change=False, address=address_index
        )
        # Drive Ethereum BIP44HDWallet
        bip44_hdwallet.from_path(path=bip44_derivation)
        # Print address_index, path, address and private_key
        print(f"{bip44_hdwallet.address()} 0x{bip44_hdwallet.private_key()}")
        # Clean derivation indexes/paths
        bip44_hdwallet.clean_derivation()


if __name__ == '__main__':
    with open('助记词.txt', 'r') as file:
        text = file.read()

    lines = text.split('\n')
    reslut = []
    for line in lines:
        main(line)

