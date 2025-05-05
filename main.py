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

print(get_proxy())