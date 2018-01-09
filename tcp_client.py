import socket

IP = 'localhost'
PORT = 12345

client_socket = socket.socket()

client_socket.connect((IP, PORT))
print('connected successfuly')

client_socket.send('message'.encode())

message = client_socket.recv(1024)

print(message.decode())


client_socket.close()