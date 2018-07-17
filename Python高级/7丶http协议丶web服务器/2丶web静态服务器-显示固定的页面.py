
import sys
import socket
def handle_data(client_socket):
    recv_data = client_socket.recv(1024)

    #组织返回用户客户端浏览器的响应报头
    response_header = "HTTP/1.1 200 OK\r\n"
    response_header += "\r\n"

    #组织返回客户端浏览器的响应body
    response_body = "<h1>hello,world!<h2>"

    response = response_header + response_body

    #返回数据
    client_socket.send(response.encode("utf-8"))
    client_socket.close()
def main():
    """控制整个程序"""

    #1丶创建tcp套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #2丶绑定端口
    server_ip = ""
    server_port = 8080
    server_addr = (server_ip,server_port)
    tcp_server_socket.bind(server_addr)

    #3丶监听
    tcp_server_socket.listen(128)

    while True:
        #4丶接收用户请求accept,
        client_socket,client_addr = tcp_server_socket.accept()
        # 设置当服务器先close 即服务器端4次挥手之后资源能够立即释放，这样就保证了，下次运行程序时 可以立即绑定8080端口
        client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        #5丶接收用户数据和返回用户数据
        handle_data(client_socket)

    #6丶关闭套接字
    tcp_server_socket.close()

if __name__ == "__main__":
    main()