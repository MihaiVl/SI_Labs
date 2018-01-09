import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = "localhost" # Get local machine name
port = 12345                 # Reserve a port for your service.

s.connect((host, port))
f = open('tosend.jpeg','rb')
print ('Sending...')
l = f.read(2048)
while (l):
    print ('Sending...')
    s.send(l)
    l = f.read(2048)
f.close()
print ("Done Sending")
s.shutdown(socket.SHUT_WR)
print (s.recv(2048))
s.close()