import socket
from str_service import CLOSE_SERVER, STR_DELIMITER


class Client:
    def __init__(self, host=None, port=None):
        self.host = host
        self.port = port

    def send(self, data):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.host, self.port))
        s.sendall(data.encode())
        answer = s.recv(1024)
        return answer.decode('utf-8')

    def api(self, fun, *args):
        strs = [str(s) for s in args]
        return self.send(STR_DELIMITER.join([fun] + strs))

    def close_server(self):
        answer = self.api(CLOSE_SERVER)
        return answer


if __name__ == '__main__':
    client = Client('127.0.0.1', 65000)
    print(client.api('reverse', 'me gusta mucho'))
    print(client.api('upper', 'me gusta mucho'))
    print(client.api('lower', 'me gusta mucho'.upper()))
    print(client.api('multiply', 'me gusta mucho', 3))
    print(client.close_server())

