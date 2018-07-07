# Author: wangfang

import socket

def main():
    #1丶创建套接字
    client_tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #2丶服务器ip和端口
    server_ip = "192.9.191.204"
    server_port = 8080

    #3丶连接服务器端
    client_tcp_socket.connect((server_ip,server_port))

    #4丶输入需要下载的文件名
    download_filename = input("请输入要下载的文件名：")


    #5丶向服务器端传输需要的下载文件
    client_tcp_socket.send(download_filename.encode("utf-8"))

    #6丶接收数据
    recv_data = client_tcp_socket.recv(1024)

    #7丶接收数据保存到文件中
    if recv_data:
        with open("[新]" + download_filename,"wb") as f:
            f.write(recv_data)

    #8丶关闭套接字
    client_tcp_socket.close()


if __name__ == "__main__":
    main()

