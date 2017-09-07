#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandom-rhodes/fopnp/blob/mn/py3/chapter03/tcp_sixteen.py

if __name__ == '__main__':
    choices = {'client':client, 'server':server}
    parser = argparse.ArgumentParser(description="Send and receive over TCP")
    parser.add_argument('role', choices = choices, help = 'while role to play')
    parser.add_argument('host', help='interface the server listens at;'
                                    'host the client sends to')
    parser.add_argument('-p', metavar="PORT", type=int, default=1060,
                        help='TCP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p)
