# Author: wangfang
# Author: wangfang

import socket
import re
import threading

class TcpHttpServer(object):
    def __init__(self,server_addr):
        self.addr = server_addr
        # 创建tcp套接字
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 绑定端口
        self.tcp_server_socket.bind(self.addr)

        # 监听
        self.tcp_server_socket.listen(128)

        # 允许立即使用上次绑定的port
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


    def handle_data(self,client_socket):
        recv_data = client_socket.recv(1024)

        # 接收的数据进行解码
        recv_data = recv_data.decode("utf-8")

        # 接收的数据进行合并
        recv_data = recv_data.splitlines()

        # 获取请求头中的URI
        url = re.match("[^/]+(/[^ ]*)", recv_data[0]).group(1)
        print(url)
        # 如果路径是/  修改路径为/index.html
        if url == "/":
            url = "/index.html"

        # 读取文件，没有不存在，执行异常代码
        try:
            f1 = open("./html" + url, "rb")
        except:
            response_header = "http/1.1 404 not found \r\n"
            response_header += "\r\n"
            response_body = "file not found".encode("utf-8")
        else:
            response_header = "http/1.1 200 OK \r\n"
            response_header += "\r\n"
            response_body = f1.read()
            f1.close()

        # 向客户端返回报头和body
        client_socket.send(response_header.encode("utf-8"))
        client_socket.send(response_body)
        # 关闭套接字
        client_socket.close()

    def server_accept(self):
        while True:
            "循环运行web服务器，等待客户端的链接并为客户端服务"
            client_socket, client_addr = self.tcp_server_socket.accept()
            t1 = threading.Thread(target=self.handle_data,args=(client_socket,))

            t1.start()
            # 因为线程是共享同一个套接字，所以主线程不能关闭，否则子线程就不能再使用这个套接字了
            # client_socket.close()
def main():
    """控制整个程序"""
    server_addr = (host,port) = "",8080
    httpd =  TcpHttpServer(server_addr)
    httpd.server_accept()


if __name__ == "__main__":
    main()