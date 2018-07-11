# Author: wangfang

import socket

def handle_data(client_socket):
    recv_data = client_socket.recv(1024)

    response_header = "http/1.1 200 OK \r\n"
    response_header += "\r\n"

    with open(r"index.html","rb")as f1:
        response_body = f1.read()

    client_socket.send(response_header.encode("utf-8"))
    client_socket.send(response_body)
    client_socket.close()
def main():
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    server_ip = ""
    server_port = 8080
    server_addr = (server_ip,server_port)

    tcp_server_socket.bind(server_addr)

    tcp_server_socket.listen(128)

    while True:
        client_socket,client_addr = tcp_server_socket.accept()
        handle_data(client_socket)

    tcp_server_socket.close()
if __name__ == "__main__":
    main()