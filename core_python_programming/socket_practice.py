import time
from socket import*


HOST=''
PORT=54354
BUFSIZ=1024
ADDR=(HOST,PORT)

tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection ...')
    tcpCliSock,addr = tcpSerSock.accept()
    print('...connected from:',addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpClisock.send('[%s] %s ' %(bytes(time.ctime(),'utf-8'),data))

    tcpCliSock.close()
tcpSerSock.close()
