#!/usr/bin/env python3
import socket               # Import socket module
import argparse
import time

s = socket.socket()         # Create a socket object
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Parse args
parser = argparse.ArgumentParser(description='Run server')
# --host
# parser.add_argument('--host', default=socket.gethostname(), type=str,
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print("host_name: %s" % host_name)
print("host_ip: %s" % host_ip)

parser.add_argument('--host', default=host_ip, type=str,
                    help='host to connect to')
# --port
parser.add_argument('--port', default=12345, type=int,
                    help='host port to connect to')

args = parser.parse_args()

host = args.host
port = args.port

print("host: %s" % host)
print("port: %s" % port)

def handle(c, addr):
   print('Got connection from', addr)
   c.send(('Thank you for connecting to ' + host).encode('utf-8'))
   echo_variable = c.recv(1024).decode('utf-8')
   print('They said', echo_variable)
   time.sleep(10)
   c.send(('You said ' + echo_variable).encode('utf-8'))
   c.close()                # Close the connection

s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   handle(c, addr)
