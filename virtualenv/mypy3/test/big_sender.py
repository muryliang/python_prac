#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandom-rhodes/fopnp/blob/mn/py3/chapter02/udp_local.py

import argparse, socket, sys

class IN:
    IP_MTU = 14
    IP_MTU_DISCOVER = 10
    IP_PMTUDISC_DO = 2

if sys.platform != 'linux':
    print('Unsupported: Can only perform MTU discovery on Linux',
          file=sys.stderr)
    sys.exit(1)

if not hasattr(IN, 'IP_MTU'):
    raise RuntimeError('cannot perform MTU discovery on this combination'
                        ' of operating system and Python distribution')
def send_big_datagram(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.IPPROTO_IP, IN.IP_MTU_DISCOVER, 0)
#    sock.connect((host, port))
    try:
        sock.sendto(b'#' * 65507, (host, port))
    except socket.error:
        print ("alas, the datagram did not make it")
        status = sock.getsockopt(socket.IPPROTO_IP, IN.IP_MTU_DISCOVER)
        max_mtu = sock.getsockopt(socket.IPPROTO_IP, IN.IP_MTU)
        print ('Actual MTU: {}'.format(max_mtu), status)
    else:
        print ('The big datagram was send!')
        status = sock.getsockopt(socket.IPPROTO_IP, IN.IP_MTU_DISCOVER)
        max_mtu = sock.getsockopt(socket.IPPROTO_IP, IN.IP_MTU)
        print ('Actual MTU: {}'.format(max_mtu), status)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Send UDP packet to get MTU')
    parser.add_argument('host', help='the host to which to target the packet')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='UDP PROT (default 1060)')
    args = parser.parse_args()
    send_big_datagram(args.host, args.p)
