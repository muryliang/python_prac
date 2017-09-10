#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandom-rhodes/fopnp/blob/mn/py3/chapter06/safe_tls.py

import argparse, socket, ssl

def client(host, port, cafile=None):
    purpose = ssl.Purpose.SERVER_AUTH
    context = ssl.create_default_context(purpose, cafile=cafile)

    raw_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    raw_sock.connect((host, port))
    ssl_sock = context.wrap_socket(raw_sock, server_hostname=host)
    while True:
        data = ssl_sock.recv(1024)
        if not data:
            break
        print (repr(data))

def server(host, port, certfile, cafile=None):
    purpose = ssl.Purpose.CLIENT_AUTH
    context = ssl.create_default_context(purpose, cafile=cafile)
    context.load_cert_chain(certfile)

    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind((host, port))
    listener.listen(1)
    print('Listening at interface {!r} and port {}'.format(host, port))
    raw_sock, address = listener.accept()
    print('Connection from host{!r} and port {}'.format(*address))
    ssl_sock = context.wrap_socket(raw_sock, server_side=True)
    ssl_sock.sendall('Simple is better than complex.'.encode('ascii'))
    ssl_sock.close()


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
