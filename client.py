#!/usr/bin/env python3
import socket
import argparse

s = socket.socket()

# Parse args
parser = argparse.ArgumentParser(description='Connect to server')
# --host
parser.add_argument('--host', default=socket.gethostname(), type=str,
                    help='host to connect to')
# --port
parser.add_argument('--port', default=12345, type=int,
                    help='host port to connect to')

args = parser.parse_args()
host = args.host
port = args.port

s.connect((host, port))
print(s.recv(1024).decode('utf-8'))
s.close()
