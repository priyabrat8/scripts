#!/usr/bin/python

import socket
import threading

def handle_client(client_socket, remote_host, remote_port):
    # Connect to the remote host
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_socket.connect((remote_host, remote_port))

    # Forward data between client and remote host
    while True:
        # Receive data from client
        client_data = client_socket.recv(4096)
        if not client_data:
            break

        elif client_data:
            print(client_data)
        # Send data to remote host
        remote_socket.sendall(client_data)

        # Receive response from remote host
        remote_data = remote_socket.recv(4096)
        if not remote_data:
            break

        elif remote_data:
            print(remote_data)

        # Send response back to client
        client_socket.sendall(remote_data)

    # Close connections
    client_socket.close()
    remote_socket.close()

def start_proxy(local_host, local_port, remote_host, remote_port):
    # Create a listening socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((local_host, local_port))
    server_socket.listen(5)
    print(f'[*] Listening on {local_host}:{local_port}')

    while True:
        # Accept incoming connections from clients
        client_socket, addr = server_socket.accept()
        print(f'[*] Accepted connection from {addr[0]}:{addr[1]}')

        # Start a new thread to handle the client connection
        proxy_thread = threading.Thread(target=handle_client, args=(client_socket, remote_host, remote_port))
        proxy_thread.start()

if __name__ == '__main__':
    # Set up port forwarding parameters
    local_host = '127.0.0.1'  # Local host
    local_port = 8888  # Local port to listen on
    remote_host = 'example.com'  # Remote host
    remote_port = 80  # Remote port to forward to

    # Start the proxy server
    start_proxy(local_host, local_port, remote_host, remote_port)
