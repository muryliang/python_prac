#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandom-rhodes/fopnp/blob/mn/py3/chapter05/streamer.py

import socket
from argparse import ArgumentParser
import argparse

def server(address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(1)
    print('Run this script in another window with "-c" to connect')
    print('listening at {}'.format(sock.getsockname()))
    sc, sockname = sock.accept()
    print ('Accepted connection from', sockname)
    sc.shutdown(socket.SHUT_WR)
    message = b''
    while True:
        more = sc.recv(8192)
        if not more:
            print('Received zero bytes -end of fle')
            break
        print('Received {} bytes'.format(len(more)))
        message += more
    print('message:\n')
    print (message.decode('ascii'))
    sc.close()
    sock.close()

def client(address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)
    sock.shutdown(socket.SHUT_RD)
    sock.sendall(b'Beautiful is better than ugly.\n')
    sock.sendall(b'Explicit is beeter than implicit.\n')
    sock.sendall(b'Simple is beeter than complex.\n')
    sock.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Send and receive over TCP")
    parser.add_argument('hostname', nargs='?', default='127.0.0.1',
            help='IP address or hostname (default: %(default)s)')
    parser.add_argument('-c', action='store_true', help='run as the client')
    parser.add_argument('-p', type=int, metavar='port', default=1060, help='TCP port number (default: %(default)s)')
    args = parser.parse_args()
    function = client if args.c else server
    function((args.hostname, args.p))
