import socket

s = socket.socket()
host = socket.gethostname()
port = 1234

s.connect(('127.0.0.1', port))
print s.recv(1024)
