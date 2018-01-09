import socket

UDP_IP = 'localhost'
UDP_PORT= 12345

message = 'Yes, this is dog.'


udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_socket.sendto(message.encode(),(UDP_IP,UDP_PORT))