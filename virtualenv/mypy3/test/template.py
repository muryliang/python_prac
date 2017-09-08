#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandom-rhodes/fopnp/blob/mn/py3/chapter05/streamer.py

import socket
from argparse import ArgumentParser
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Send and receive over TCP")
    parser.add_argument('hostname', nargs='?', default='127.0.0.1',
            help='IP address or hostname (default: %(default)s)')
    parser.add_argument('-c', action='store_true', help='run as the client')
    parser.add_argument('-p', type=int, metavar='port', default=1060, help='TCP port number (default: %(default)s)')
    args = parser.parse_args()
    function = client if args.c else server
    function((args.hostname, args.p))
