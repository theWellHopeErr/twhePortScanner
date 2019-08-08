#!usr/bin/python

import socket
import os
from sys import exit

def retBanner(ip_address,port):
     try:
          s=socket.socket()
          s.connect((ip_address,port))
          return s.recv(1024)
     except:
          return

def checkVulns(banner,file):
	f = open(filename,'r')
	for line in f.readlines():
		if line.strip('\n') in banner:
			print('[+] Server is vulnerable: ' + banner.strip('\n') )

def main():
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		if not os.path.isFile(filename):
			print('[-] File Doesn\'t Exist')
		if not os.access(filename, os.R_OK):
			print('[-] Access Denied')
			sys.exit()
	else:
		print('[-] Usage: '+str(sys.argv[0])
		sys.exit()
	portlist = [21,22,25,80,443]
	for x in range(1,6):
		ip = '192.168.1." + str(x)
		for port in portlist:
			banner = retBanner(ip,port)
			if banner:
				print('[+]'+ip+'/'+str(port)+':'+banner)
				checkVulns(banner,filename)

main()
