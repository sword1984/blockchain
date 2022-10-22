"""
@author: Sword
@email: 173963781@qq.com
@site: 
@file: example.py
@time: 2022/10/13 10:20
"""
from web3 import Web3
import json
import time
import os
import logging
from decimal import Decimal


class PayEthOrToken(object):

    def __init__(self):
        # 设置web3
        self.web3 = Web3(Web3.HTTPProvider('your infura http url'))
        # token合约地址
        self.contract_address = 'your contract address'
        # 主钱包地址
        self.wallet = 'your wallet address'
        # 钱包的私钥
        self.wallet_key = 'your wallet key'
        # 合约的abi test.json 是eth的abi json文件，可以在eth区块链浏览器上获得
        with open('test.json', 'r') as f:
            self.abi = json.loads(f.read())
        # 生成合约
        self.contract = self.web3.eth.contract(address=self.contract_address, abi=self.abi)
        # 代币简写
        self.token_name = 'USDT'

    def transfer_usdt(self, to, value):
        '''进行代币转账
        args：
            to str：接收代币的地址
            value str/int：代币数量，以ether为单位，可以是字符串和int类型
        returns：
            (str, str)：返回交易哈希，以及异常信息
        '''
        try:
            token_balance = self.web3.fromWei(self.contract.functions.balanceOf(self.wallet).call(), 'ether')
            # 如果代币不足返回异常
            if Decimal(token_balance) < Decimal(value):
                return None, 'Platform USDT token is insufficient, please try again later'
            # 进行转账代币
            nonce = self.web3.eth.get_transaction_count(self.wallet)
            tx = {
                'from': self.wallet,
                'nonce': nonce,
                'gas': 100000,
                'gasPrice': self.web3.toWei('50', 'gwei'),
                'chainId': 1
            }
            to = Web3.toChecksumAddress(to)
            txn = self.contract.functions.transfer(to, self.web3.toWei(value, 'ether')).buildTransaction(tx)
            signed_txn = self.web3.eth.account.sign_transaction(txn, private_key=self.wallet_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            return self.web3.toHex(tx_hash), 'pay success'
        except Exception as e:
            logging.error(f'转账{self.token_name}代币时发生异常：{e}')
            logging.exception(e)
            return None, str(e)

    def transfer_eth(self, to, value):
        '''进行eth转账
        args：
            to str：接收以太坊的地址
            value str/int：数量，以ether为单位，可以是字符串和int类型
        returns：
            str：返回交易哈希
        '''
        try:
            token_balance = self.web3.fromWei(self.web3.eth.get_balance(self.wallet), 'ether')
            # 如果代币不足返回异常
            if Decimal(token_balance) < Decimal(value):
                return None, 'Platform ETH token is insufficient, please try again later'
            # 获取 nonce，这个是交易计数
            to = Web3.toChecksumAddress(to)
            nonce = self.web3.eth.get_transaction_count(self.wallet)
            tx = {
                'nonce': nonce,
                'to': to,
                'gas': 100000,
                'gasPrice': self.web3.toWei('50', 'gwei'),
                'value': self.web3.toWei(value, 'ether'),
                'chainId': 1
            }
            # 签名交易
            signed_tx = self.web3.eth.account.sign_transaction(tx, self.wallet_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            return self.web3.toHex(tx_hash), 'pay success'
        except Exception as e:
            logging.error(f'转账eth时发生异常：{e}')
            logging.exception(e)
            return None, str(e)


if __name__ == '__main__':
    import re
