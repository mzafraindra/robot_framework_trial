import serverlib
import clientlib


server = serverlib.ServerLib('127.0.0.1', 65000)
client = clientlib.ClientLib('127.0.0.1', 65000)

server.receive_one()
a = client.reverse('me gusta')


print(client._result)