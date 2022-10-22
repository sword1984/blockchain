# encoding:utf-8

"""
 @Author: chenj
 @Email: 173963781@qq.com
 @FileName: tutorials.py
 @DateTime: 2022/10/20 16:55
"""

from web3 import Web3

# rpc服务提供商 infura.io
infura_url = 'https://mainnet.infura.io/v3/21d15e8f8daf4043afe66015fa07e9db'
w3 = Web3(Web3.HTTPProvider(infura_url))

if __name__ == '__main__':
    pass
