import time
from socketserver import TCPServer,BaseRequestHandler as BRH



HOST = ''
PORT = 1999
ADDR = (HOST,PORT)
BUFSIZ = 1024

class MyRequestHandler(BRH):
    def handle(self):
        print(self.request)
        self.data = self.request.recv(1024).strip()
        print('{} wrote:'.format(self.client_address[0]))
        print(self.data)
        self.request.sendall(self.data.upper())

with TCPServer((HOST,PORT),MyRequestHandler) as server:
    print('waiting for connection...')
    server.serve_forever()
