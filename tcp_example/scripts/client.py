import socket
import sys, os
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 8080  # The port used by the server

def main():
    # while 1:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            # s.sendall(b"Hello, world")
            data = s.recv(1024)

        print(f"Received {data!r}")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)