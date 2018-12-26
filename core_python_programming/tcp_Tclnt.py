from socket import *

HOST='macbook-air'#use the hostname of server
PORT=54353
BUFSIZ=1024
ADDR=(HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(bytes(data,'utf-8'))
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))
tcpCliSock.close()
