#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandom-rhodes/fopnp/blob/mn/py3/chapter02/udp_remote.py

import argparse, socket, random, sys, time
from datetime import datetime

MAX_BYTES = 65535

def server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#    sock = socket.socket()
    sock.bind(('localhost', port))
    print('Listening at {}'.format(sock.getsockname()))
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        if random.random() < 0.4:
            print ("drop packet from {}".format(address))
            continue
        text = data.decode('ascii')
        print('The client at {} says {!r}'.format(address, text))
        text = 'Your data was {} bytes long'.format(len(data))
        data = text.encode('ascii')
        sock.sendto(data, address)

def client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect(("localhost", port)) # connect to server
    print ("peer name is", sock.getpeername())
    print('The OS assigned me the address {}'.format(sock.getsockname()))
    delay = 0.1
    text = 'The time is {}'.format(datetime.now())
    data = text.encode('ascii')
    while True:
        sock.send(data,)
        print ("waiting up to {} seconds for a reply".format(delay))
        sock.settimeout(delay)
        try:
            data = sock.recv(MAX_BYTES)
        except socket.timeout:
            delay *= 2
            if delay > 2:
                raise RuntimeError("I think the server is down")
        else:
            break
        print ('The server replied {!r}'.format(data.decode('ascii')))

if __name__ == "__main__":
    choices = {'client':client, 'server':server}
    parser = argparse.ArgumentParser(description='Send and receive UDP locally')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                    help='UDP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.p)

