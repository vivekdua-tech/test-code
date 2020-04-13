import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto('The world is yours!'.encode(), ('localhost', 9606))
s.close()

