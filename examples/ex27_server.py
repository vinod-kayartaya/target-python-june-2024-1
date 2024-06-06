#! .venv/bin/python
from socket import socket, AF_INET, SOCK_STREAM
import threading


def handle_client(cl_sock, cl_addr):
    print(f'got a connection from {cl_addr}')
    message = 'Hello and welcome'
    cl_sock.send(message.encode())
    filename = cl_sock.recv(1024).decode()
    with open(filename) as f:
        cl_sock.send(f.read().encode())
    cl_sock.close()

def main():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_addr = ('192.168.1.23', 2345)
    server_socket.bind(server_addr)
    server_socket.listen(5)
    print(f'server started at {server_addr}')

    while True:
        print('waiting for a client connection...')
        cl_sock, cl_addr = server_socket.accept()
        threading.Thread(target=handle_client, args=(cl_sock, cl_addr)).start()


if __name__ == '__main__':
    main()

