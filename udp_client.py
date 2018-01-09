import socket

UDP_IP = 'localhost'
UDP_PORT= 12345


udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_socket.bind((UDP_IP,UDP_PORT))

message, addr = udp_socket.recvfrom(1024)

print (message)