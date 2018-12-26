import time
from socket import*


HOST=''
PORT=43441
BUFSIZ=1024
ADDR=(HOST,PORT)

udpSerSock=socket(AF_INET,SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print('waiting for connected...')
    data,addr = udpSerSock.recvfrom(BUFSIZ)
    data=data.decode('utf-8')
    data=data*5
    udpSerSock.sendto(bytes(data,'utf-8'),addr)
    print('received from and return:',addr)

udpSerSock.close()
