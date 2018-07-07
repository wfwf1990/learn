# Author: wangfang
import socket

def send_file_2_client(client_socket,client_addr):

    file_content = None
    # 接收客户端发过来的数据
    filename = client_socket.recv(1024).decode("utf-8")
    print("客户端%s需要下载的文件是%s" %(client_addr,filename))
    #打开这个文件，读取数据
    try:
        f = open(filename,"rb")
        file_content = f.read()
        f.close()

    except Exception as ret:
        print("%s文件不存在" %filename)

    # 返回客户端数据
    if file_content:
        client_socket.send(file_content)


def main():
    #创建套接字
    server_tcp_socket  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #绑定本地ip和端口
    server_ip = "192.9.191.204"
    server_port = 8080
    server_tcp_socket.bind((server_ip,server_port))

    #监听状态listen
    server_tcp_socket.listen(128)
    while True:
        # 接收客户端请求连接accept，建立连接,返回建立连接的socket和客户端ip
        client_socket, client_addr = server_tcp_socket.accept()

        #发送数据给客户端
        send_file_2_client(client_socket,client_addr)

        # 关闭套接字
        client_socket.close()


if __name__ == "__main__":
    main()

