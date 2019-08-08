#!/usr/bin/python
import socket
def grab_banner(ip_address,port):
     try:
          s=socket.socket()
          s.connect((ip_address,port))
          return s.recv(1024)
     except:
          return

def main():
    portList = [21,22,23]
    ip_address = '192.168.1.1'
    for port in portList:
        banner = grab_banner(ip_address,port)
        print ip_address + '/' + str(port) + ':' + banner

if __name__ == '__main__':
      main()
