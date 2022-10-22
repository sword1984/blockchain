# encoding:utf-8

"""
 @Author: chenj
 @Email: 173963781@qq.com
 @FileName: erc20.py
 @DateTime: 2022/10/18 6:35
"""

import requests
from sdk import WEB3, BSCAPIKEY


class ERC20(object):
    def __init__(self, contract_address='', abi=''):
        self.contract_address = contract_address
        if abi:
            self.abi = abi
        else:
            self.abi = self.get_bsc_abi()
        self.contract = WEB3.eth.contract(address=contract_address, abi=self.abi)

    def get_bsc_abi(self):
        """通过Bscscan获取Token的Abi

        :return:
        """
        url = 'https://api.bscscan.com/api'
        data = {
            'module': 'contract',
            'action': 'getabi',
            'address': self.contract_address,
            'apikey': BSCAPIKEY
        }

        response = requests.get(url=url, data=data).json()

        if response['message'] == 'OK':
            return response['result']

    def get_balance(self, address):
        balance = self.contract.functions.balanceOf(address).call()
        return WEB3.fromWei(balance, 'ether')


if __name__ == '__main__':
    my_address = '0xD582461Ae1488cB768B42BC4f271AfD000000000'
    my_address1 = '0x01a1f994AD69c356eBbEe8879456E55488888888'
    raca = ERC20(contract_address='0x12BB890508c125661E03b09EC06E404bc9289040')
    print(raca.contract.functions.name().call())
    print(raca.contract.functions.symbol().call())
