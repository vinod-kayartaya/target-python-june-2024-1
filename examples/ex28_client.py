#! .venv/bin/python
from socket import socket, AF_INET, SOCK_STREAM


def main():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_addr = ('192.168.1.23', 2345)
    server_socket.connect(server_addr)
    msg = server_socket.recv(1024).decode()
    print(f'server says : {msg}')
    filename = input('Enter file to retrieve from server: ')
    server_socket.send(filename.encode())
    content = server_socket.recv(10240).decode()
    print(content)
    server_socket.close()

if __name__ == '__main__':
    main()

