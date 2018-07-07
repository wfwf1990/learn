# Author: wangfang
import socket

def main():

    #创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #绑定ip和port
    server_ip = "192.9.191.204"
    server_port = 8080
    tcp_server_socket.bind((server_ip,server_port))

    #listen状态，使用套接字变为被动连接，接收客户端请求
    tcp_server_socket.listen(128)

    # 循环目的：调用多次accept,从而为多个客户端服务
    while True:
        # accept等待客户端的连接，会返回一个元祖
        # 当建立连接的时候，server端会重新创建一个socket，
        # client_socket用来为这个客户端服务
        client_socket, client_addr = tcp_server_socket.accept()
        print("一个新的客户端已经到来%s" %str(client_addr))

        # 循环目的: 为同一个客户端 服务多次
        while True:
            # 接收对方发送过来的请求数据
            # 接收对方发送过来的数据是使用新创建的socket进行接收
            recv_data = client_socket.recv(1024)
            print(recv_data.decode("utf-8"))

            #如果recv解堵塞，那么有两种方式
            #1.客户端主动发送数据关闭
            #2.客户端嗲用close导致
            if recv_data:
                # 给对方发送数据
                send_data = client_socket.send("hahaha".encode("utf-8"))
            else:
                # 关闭套接字
                # 关闭accept返回的套接字，意味着不会为这个客户端服务
                client_socket.close()
                print("服务器端已经关闭了")
                break

    #如果将监听套接字关闭，那么会导致整个程序都不会为新的客户端的请求连接做服务
    tcp_server_socket.close()

if __name__ == "__main__":
    main()