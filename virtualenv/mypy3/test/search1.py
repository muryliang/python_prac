#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandom-rhodes/fopnp/blob/mn/py3/chapter01/search1.py

from pygeocoder import Geocoder
if __name__ == "__main__":
#    address = '207 N. Defiance St, Archbold, OH'
    address = 'SuZhou, JangSu, China'
    print(Geocoder.geocode(address)[0].coordinates)
