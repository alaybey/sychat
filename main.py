import socket
import threading
import sys

#############################
# Author by Ibrahim Alaybeyi ##
# BY GPL ##
# 2016#
#############################


# Server side
class Server:
    sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sck.bind((socket.gethostname(), 1234))
    sck.listen(5)
    connects = []

    def __init__(self):
        self.sck.bind(('0.0.0.0', 10000))
        self.sck.listen(1)

#  Create a data/msg
    def handler(self, con):
        while True:
            data = con.recv(1024)
            for connection in self.connects:
                connection.send(data)

        # create a connect and send
    def exec(self):
        while True:
            con = self.sck.accept()
            addr = self.sck.accept()
            print(f"connection from {addr}")
            conThread = threading.Thread(target=self.handler, args=(con, addr))
            conThread.daemon = True
            conThread.start()
            connection.append(con)
            print(connection)

#client side
class Client:
    sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sck.connect((socket.gethostname(), 1234))
    def message(self):
        while True:
            self.sck.send(bytes(input(""), 'utf-8'))

#   create a connect and show
    def __init__(self, address):
        self.sck.connect((address, 10000))

        clThread = threading.Thread(target=self.message)
        clThread.daemon = True
        clThread.start()
        while True:
            msg = self.sck.recv(16)
            print(msg)


client = Client()
srv = Server()
srv.exec()
