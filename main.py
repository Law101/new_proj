import os
import sys
import json
import requests
import time
import random

def get_proxy():
    url = "http://api.ip.data5u.com/dynamic/get.html?order=970505113258629&sep=3"
    response = requests.get(url)
    proxy = response.text.strip()
    return proxy

def get_proxy_list():
    url = "http://api.ip.data5u.com/dynamic/get.html?order=970505113258629&sep=3"
    response = requests.get(url)
    proxy_list = response.text.strip().split('\n')
    return proxy_list


print(get_proxy())