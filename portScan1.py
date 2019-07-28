# !usr/bin/python

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "192.168.1.4"
port = 444
def portScan(port):
	if sock.connect_ex((host,port)):
		print("Port %d is closed" % (port))
	else:
		print("Port %d is open" % (port))

portScan(port)
