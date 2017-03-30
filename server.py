__author__ = 'uva'

import SocketServer


class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024)
        while len(self.data):
            print(
            'Client connected with ip address {} and port {}'.format(self.client_address[0], self.client_address[1]))
            print 'Recieved data from client {}'.format(self.data)
            self.request.send(self.data.upper())
            self.data = self.request.recv(1024)

    def finish(self):
        print 'Client Leaving.... and Left !!!'


if __name__ == '__main__':
    pair = 'localhost', 8080
    # Allow fast recycle and reusing
    SocketServer.TCPServer.allow_reuse_address = True
    server = SocketServer.TCPServer(pair, MyTCPHandler)
    SocketServer.TCPServer.allow_reuse_address = True
    server.serve_forever()