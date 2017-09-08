#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandom-rhodes/fopnp/blob/mn/py3/chapter04/www_ping.py

import argparse, socket, sys

def connect_to(hostname_or_ip):
    try:
        infolist = socket.getaddrinfo(
                hostname_or_ip, 'www', 0, socket.SOCK_STREAM, 0,
                socket.AI_ADDRCONFIG | socket.AI_V4MAPPED | socket.AI_CANONNAME
        )
    except socket.gaierror as e:
        print ('Name servie failure:', e.args[1])
        sys.exit(1)

    info = infolist[0] # get the first addr info
    socket_args = info[:3]
    address = info[4]
    s = socket.socket(*socket_args)
    try:
        s.connect(address)
    except socket.error as e:
        print('Network failure:', e.args[1])
    else:
        print ('Success: host', info[3], 'is listening on port 80')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="try connecting on port 80")
    parser.add_argument('hostname', help='hostname you want to connect')
    connect_to(parser.parse_args().hostname)
