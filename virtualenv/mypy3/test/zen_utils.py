#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandom-rhodes/fopnp/blob/mn/py3/chapter07/zen_utils.py

import socket, argparse, time

aphorisms = {b'Beautiful is better than?': b'Ugly.',
        b'Explicit is better than?' : b'Implicit.',
        b'Simple is better than?': b'Complex.'}

def get_answer(aphorism):
    """Return the string response to a particular Zen-of-Python aphorism."""
    time.sleep(0.0) 
    return aphorisms.get(aphorism, b'Error: unknow aphorism.')

def parse_command_line(description):
    """parse command line and return a socket address"""
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('host', help='IP or hostname')
    parser.add_argument('-p', metavar='port', type=int, default=1060,
                        help="tcp port (default 1060)")
    args = parser.parse_args()
    address = (args.host, args.p)
    return address

def create_srv_socket(address):
    """Build and return a listening server socket."""
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind(address)
    listener.listen(64)
    print('Listening at  {}'.format(address))
    return listener

def accept_connections_forever(listener):
    while True:
        sock, address = listener.accept()
        print('Accept connection from {}'.format(address))
        handle_conversation(sock, address)

def handle_conversation(sock, address):
    try:
        while True:
            handle_request(sock)
    except EOFError:
        print('client socket to {} has closed'.format(address))
    except Exception as e:
        print('client {} error: {}'.format(address, e))
    finally:
        sock.close()

def handle_request(sock):
    aphorism = recv_until(sock, b'?')
    answer = get_answer(aphorism)
    sock.sendall(answer)

def recv_until(sock, suffix):
    message = sock.recv(4096)
    if not message:
        raise EOFError('socket closed')
    while not message.endswith(suffix):
        data = sock.recv(4096)
        if not data:
            raise IOError('received {!r} then socket closed'.format(message))
        message += data
    return message

if __name__ == "__main__":
    addr = parse_command_line("this is a command line server")
    accept_connections_forever(create_srv_socket(addr))
