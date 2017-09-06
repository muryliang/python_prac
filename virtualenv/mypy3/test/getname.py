#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandom-rhodes/fopnp/blob/mn/py3/chapter01/getname.py

import socket

if __name__ == "__main__":
    hostname = 'www.python.org'
    addr = socket.gethostbyname(hostname)
    print ("The Ip address of {} is {}".format(hostname, addr))
