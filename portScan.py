# !usr/bin/python

import socket
from termcolor import colored

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	#AF_INET is used as (host,port) format is used

host = raw_input("Enter host to scan: ")
port = int(raw_input("Enter port to scan: "))

def portScan(port):
	if sock.connect_ex((host,port)): #connect_ex return 0 if connection has succeeded else returns errno
		print(colored("Port %d is closed" % (port),'red'))
	else:
		print(colored("Port %d is open" % (port),'green'))

portScan(port)
