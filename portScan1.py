# !usr/bin/python

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	#AF_INET is used to as (host,port) format is used

host = "172.16.1.185"    #IP Address of user's PC
port = 444		#Port that needs to be checked

def portScan(port):
	if sock.connect_ex((host,port)): #connect_ex return 0 if connection has succeeded else returns errno
		print("Port %d is closed" % (port))
	else:
		print("Port %d is open" % (port))

portScan(port)