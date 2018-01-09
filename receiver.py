import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = "localhost" # Get local machine name
port = 12345                 # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
f = open('torecv.jpeg','wb')
s.listen(5)                 # Now wait for client connection.
while True:
    c, addr = s.accept()     # Establish connection with client.
    print ('Got connection from', addr)
    print ("Receiving...")
    l = c.recv(2048)
    while (l):
        print ("Receiving...")
        f.write(l)
        l = c.recv(2048)
    f.close()
    print ("Done Receiving")
    c.send('Thank you for connecting'.encode('utf-8'))
    c.close() 