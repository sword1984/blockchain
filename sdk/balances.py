"""
@author: Sword
@email: 173963781@qq.com
@site: 
@file: balances.py
@time: 2022/10/14 9:57
"""

from configparser import ConfigParser
from web3 import Web3
import requests

# 读取远程提供商
cfg = ConfigParser()
cfg.read('config.ini')
provider = cfg.get('server', 'provider')

w3 = Web3(Web3.HTTPProvider(provider))
BSC_KEY = cfg.get('server', 'bsc_api_key')


def get_abi(address):
    url = 'https://api.bscscan.com/api'
    data = {
        'module': 'contract',
        'action': 'getabi',
        'address': address,
        'apikey': BSC_KEY
    }

    response = requests.get(url=url, data=data).json()

    if response['message'] == 'OK':
        return response['result']


def get_balance(address):
    balance = w3.eth.get_balance(address)
    return w3.fromWei(balance, 'ether')


def get_balance_erc20(contract_address, abi, current_address):
    token_contract = w3.eth.contract(address=contract_address, abi=abi)
    balance = token_contract.functions.balanceOf(current_address).call()
    return w3.fromWei(balance, 'ether')


if __name__ == '__main__':
    with open('addresses.txt', 'r') as file:
        text = file.read()

    lines = text.split('\n')

    total = 0
    for address in lines:
        balance = get_balance(address)
        total += balance

    print(total)