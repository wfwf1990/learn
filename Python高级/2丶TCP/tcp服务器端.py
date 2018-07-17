# Author: wangfang
import socket

def main():

    #创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #绑定ip和port
    server_ip = ""
    server_port = 8080
    tcp_server_socket.bind((server_ip,server_port))

    #listen状态，使用套接字变为被动连接，接收客户端请求
    tcp_server_socket.listen(128)

    #accept等待客户端的连接，会返回一个元祖
    #当建立连接的时候，server端会重新创建一个socket，
    #client_socket用来为这个客户端服务
    client_socket,client_addr = tcp_server_socket.accept()

    #接收对方发送过来的数据
    #接收对方发送过来的数据是使用新创建的socket进行接收
    recv_data = client_socket.recv(1024)
    print(recv_data.decode("utf-8"))

    #给对方发送数据
    send_data = client_socket.send("hahaha".encode("utf-8"))

    #关闭套接字
    tcp_server_socket.close()
    client_socket.close()

if __name__ == "__main__":
    main()