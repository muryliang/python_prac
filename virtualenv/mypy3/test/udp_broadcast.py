#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandom-rhodes/fopnp/blob/mn/py3/chapter02/udp_local.py

import argparse, socket

BUFSIZE = 65535

def server(interface, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((interface, port))
    print ('Listening for datagram at {}'.format(sock.getsockname()))
    while True:
        data, address = sock.recvfrom(BUFSIZE)
        text = data.decode("ascii")
        print ("the client at {} says: {!r}".format(address, text))

def client(network, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    text = 'Broadcast Datagrams!'
    sock.sendto(text.encode('ascii'), (network, port))

if __name__ == '__main__':
    choices = {'client':client, 'server':server}
    parser = argparse.ArgumentParser(description="Send, receive UDP broadcast")
    parser.add_argument('role', choices=choices, help="which role to take")
    parser.add_argument('host', help='interface the server listens at;'
                                    'network the client send to')
    parser.add_argument('-p', metavar="PORT", type=int, default=1060,
                        help='UDP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p)
