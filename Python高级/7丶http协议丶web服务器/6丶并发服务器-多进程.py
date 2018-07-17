# Author: wangfang
# Author: wangfang

import socket
import re
import multiprocessing

def handle_data(client_socket):
    recv_data = client_socket.recv(1024)

    #接收的数据进行解码
    recv_data = recv_data.decode("utf-8")

    #接收的数据进行合并
    recv_data = recv_data.splitlines()

    #获取请求头中的URI
    url = re.match("[^/]+(/[^ ]*)",recv_data[0]).group(1)
    print(url)
    #如果路径是/  修改路径为/index.html
    if url == "/":
        url = "/index.html"

    #读取文件，没有不存在，执行异常代码
    try:
        f1 = open("./html" +url,"rb")
    except:
        response_header = "http/1.1 404 not found \r\n"
        response_header += "\r\n"
        response_body = "file not found".encode("utf-8")
    else:
        response_header = "http/1.1 200 OK \r\n"
        response_header += "\r\n"
        response_body = f1.read()
        f1.close()

    #向客户端返回报头和body
    client_socket.send(response_header.encode("utf-8"))
    client_socket.send(response_body)
    #关闭套接字
    client_socket.close()
def main():
    """控制整个程序"""
    #创建tcp套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #绑定端口
    server_ip = ""
    server_port = 8080
    server_addr = (server_ip,server_port)
    tcp_server_socket.bind(server_addr)

    # 允许立即使用上次绑定的port
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #监听
    tcp_server_socket.listen(128)

    while True:
        """接收用户请求和返回用户数据"""
        client_socket,client_addr = tcp_server_socket.accept()

        p1 = multiprocessing.Process(target=handle_data,args=(client_socket,))
        p1.start()
        # 因为线程是共享同一个套接字，所以主线程不能关闭，否则子线程就不能再使用这个套接字了
        client_socket.close()

if __name__ == "__main__":
    main()