#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandom-rhodes/fopnp/blob/mn/py3/chapter01/search3.py

import http.client
import json
from urllib.parse import quote_plus

""" use http protocol util directly make a request instead of requests module
    in the version, you must manually construct the request url and encode necessary part
"""

base = '/maps/api/geocode/json'

def geocode(address):
    path = '{}?address={}&sensor=false'.format(base, quote_plus(address))
    connection = http.client.HTTPConnection('maps.google.com')
    connection.request('GET', path)
    rawreply = connection.getresponse().read()
    reply = json.loads(rawreply.decode('utf-8'))
    print(reply['results'][0]['geometry']['location'])

if __name__ == "__main__":
    geocode('WuXi, JiangSu, China')
