import socket
import time
import re
"""思路"""
#短连接：客户端和服务器端建立三次握手，发送和接收一次数据，就马上执行4次挥手断开
#长连接：客户端和服务器端建立三次握手，不停的发送和接收数据，客户端执行close,执行4次挥手断开

#长连接：是根据服务器端返回数据的时候，会在response_header中定义Content-Length 表示response_body的长度，这样客户端就知道数据的长度


def send_data(client_socket,recv_data):

    recv_data = recv_data.decode("utf-8")
    data = recv_data.splitlines()
    url = re.match("[^/]+(/[^ ]*)",data[0]).group(1)
    if url == "/":
        url = "/index.html"
    file_name = "./html" + url
    try:

        f1 = open(file_name,"rb")
    except:

        response_body = "<h1>file not found<h1\>"
        response_header = "http/1.1 404 not found \r\n"
        response_header += "Content-Length:%d \r\n" % len(response_body)
        response_header+= "\r\n"
        response = response_header + response_body
        client_socket.send(response.encode("utf-8"))
    else:
        response_body = f1.read()
        response_header = "http/1.1 200 ok \r\n"
        response_header += "Content-Length:%d \r\n" %len(response_body)
        response_header += "\r\n"

        response = response_header.encode("utf-8") + response_body
        client_socket.send(response)




client_socket_list = list()  # 存储所有客户端socket


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = ""
    server_port = 8080
    server_addr = (server_ip, server_port)

    tcp_server_socket.bind(server_addr)
    tcp_server_socket.listen(128)

    # 将套接字设置为非堵塞
    # 设置为非堵塞后，如果accept时，恰巧没有客户端connect，那么accept会
    # 产生一个异常，所以需要try来进行处理
    tcp_server_socket.setblocking(False)

    while True:
        time.sleep(2)
        try:
            client_socket, client_addr = tcp_server_socket.accept()
        except Exception as ret:
            print("没有客户端连接")
        else:
            print("一个新的客户端到来%s" % client_socket)
            client_socket.setblocking(False)  # 设置为非堵塞
            client_socket_list.append(client_socket)
        for client_socket_temp in client_socket_list:
            try:
                recv_data = client_socket_temp.recv(1024)
            except Exception as ret:
                print("没有收到数据...")
            else:
                print("没有异常")
                if recv_data:
                    print("客户端发来了数据")
                    send_data(client_socket_temp,recv_data)
                else:
                    client_socket_temp.close()
                    client_socket_list.remove(client_socket_temp)
                    print("客户端已经关闭")


if __name__ == "__main__":
    main()