from socket import*
import sys

HOST = 'localhost'
PORT = 1999
BUFSIZ = 1024
ADDR = (HOST,PORT)

data = input('>')

with socket(AF_INET,SOCK_STREAM) as sock:
    sock.connect((HOST,PORT))
    sock.sendall(bytes(data,'utf-8'))
    Received = sock.recv(1024).decode('utf-8')

print('send:   {}'.format(data))
print('received:  {}'.format(Received))
