import socket
from time import sleep
import xml.etree.ElementTree as ET
import sys
import os

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 8080  # Port to listen on (non-privileged ports are > 1023)
with open('/home/gbily/workspace/tcp_example/scripts/cmd.xml', 'r') as f:
    data = f.read() 




if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    print(f"Connected by {addr}")
    while True:
        data = conn.recv(65536)
        if not data:
            break
        print(data)
    f = open('/home/gbily/workspace/nodered/status.txt', 'ab')
    print(data.decode())
    f.write(data.decode()) 
    # conn.sendall(data.encode())
    s.close()