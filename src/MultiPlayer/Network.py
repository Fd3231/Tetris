import socket


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "127.0.0.1"
        self.port = 65032
        self.addr = (self.server, self.port)
        self.id = self.connect()

    def getId(self):
        return self.id

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(data.encode(encoding='UTF-8'))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)