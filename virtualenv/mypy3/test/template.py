#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandom-rhodes/fopnp/blob/mn/py3/chapter07/zen_utils.py

import socket
from argparse import ArgumentParser
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Safe tls cliednt and server")
    parser.add_argument('host', help='IP address or hostname' )
    parser.add_argument('port', type=int, help='tcp port number')
    parser.add_argument('-a', metavar ='cafile', default=None,
                            help='authority: path to CA certificate PEM file')
    parser.add_argument('-s', metavar='certifile', default=None, 
                        help='run as server: apth to server PEM file')
    args = parser.parse_args()
    if args.s:
        server(args.host, args.port, args.s, args.a)
    else:
        client(args.host, args.port, args.a)
