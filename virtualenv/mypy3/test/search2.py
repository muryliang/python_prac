#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandom-rhodes/fopnp/blob/mn/py3/chapter01/search2.py

"""in this version, you send the detail url and params seperately into requests function,
    it will help you encode and combine them
"""

import requests

def geocode(address):
    parameters = {'address':address, 'sensor':'false'}
    base = 'http://maps.googleapis.com/maps/api/geocode/json'
    response = requests.get(base, params=parameters)

    answer = response.json()
    print (answer)
    print (answer['results'][0]['geometry']['location'])

if __name__ == "__main__":
    geocode('WuXi, JiangSu, China')
