import socket
from str_service import CLOSE_SERVER, STR_DELIMITER
import str_service.utils as utils


class Server:
    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host, port))
        self.socket.listen()

        self.handlers = {'upper': utils.upper,
                         'lower': utils.lower,
                         'reverse': utils.reverse,
                         'multiply': lambda s, n: utils.multiply(s, int(n)),
                         CLOSE_SERVER: lambda: 'Server closing...'}

    def __del__(self):
        self.socket.close()

    @staticmethod
    def parse(data):
        s = data.decode('utf-8').split(STR_DELIMITER)
        return s[0], s[1:]

    def receive_one(self):
        socket_with_client, client_addr = self.socket.accept()
        with socket_with_client:
            data = socket_with_client.recv(1024)
            fun, args = self.parse(data)
            answer = self.handlers[fun](*args).encode()
            socket_with_client.sendall(answer)
            return fun, args

    def receive(self, n):
        data = []
        for i in range(n):
            data.append(self.receive_one())
        return data

    def run(self):
        data = ('', '')
        while data[0] != CLOSE_SERVER:
            data = self.receive_one()


if __name__ == '__main__':

    server = Server('127.0.0.1', 65000)
    server.run()