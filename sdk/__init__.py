# encoding:utf-8

"""
 @Author: chenj
 @Email: 173963781@qq.com
 @FileName: __init__.py.py
 @DateTime: 2022/10/18 11:35
"""

from configparser import ConfigParser
from web3 import Web3

# 远程提供商
cfg = ConfigParser()
cfg.read('config.ini')
PROVIDER = cfg.get('server', 'provider')
BSCAPIKEY = cfg.get('server', 'bsc_api_key')

WEB3 = Web3(Web3.HTTPProvider(PROVIDER))
