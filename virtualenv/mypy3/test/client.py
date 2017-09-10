#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandom-rhodes/fopnp/blob/mn/py3/chapter07/client.py

import socket, argparse, random, zen_utils

def client(address, cause_error=False):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)
    aphorisms = list(zen_utils.aphorisms)
    if cause_error:
        sock.sendall(aphorisms[0][:-1])
        return
    for aphorisms in random.sample(aphorisms,3):
        sock.sendall(aphorisms)
        print(aphorisms, zen_utils.recv_until(sock, b'.'))
    sock.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="example client")
    parser.add_argument('host', help='IP address or hostname' )
    parser.add_argument('-p', metavar="port", type=int, default=1060, help='tcp port number')
    parser.add_argument('-e', action='store_true',  help='cause error')
    args = parser.parse_args()
    address = (args.host, args.p)
    client(address, args.e)
