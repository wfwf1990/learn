# Author: wangfang

import socket
def main():
    #创建套接字
    tcp_client_socket =socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #服务器端ip和端口
    server_ip = "192.9.191.204"
    server_port = 8080

    #连接服务器
    tcp_client_socket.connect((server_ip,server_port))      #元祖

    #输入要发送的数据
    send_data = input("请输入要发送的数据:")
    #发送数据
    tcp_client_socket.send(send_data.encode("utf-8"))

    #关闭套接字
    tcp_client_socket.close()


if __name__ == "__main__":
    main()