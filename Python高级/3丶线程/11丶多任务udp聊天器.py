# Author: wangfang
import socket
import threading

def recv_msg(server_udp_socket):
    """接收数据"""
    while True:
        recv_data = server_udp_socket.recvfrom(1024)
        print(recv_data)

        client_msg = recv_data[0]  # 数据是二进制
        client_addr = recv_data[1]  # 客户端ip和端口是元祖
        print("客户端%s:发过来的数据是：%s" % (str(client_addr), client_msg.decode("gbk")))

def send_msg(server_udp_socket,client_ip,client_port):
    """返回数据"""
    while True:
        send = input("请输入你要回复的消息:")
        if send != "q":
            send_data = server_udp_socket.sendto(send.encode("gbk"),(client_ip,client_port))
        else:
            break
            server_udp_socket.close()

def main():
    #创建套接字
    server_udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    #绑定端口
    server_ip = "192.9.191.213"
    server_port = 8080
    server_udp_socket.bind((server_ip,server_port))

    #获取客户端ip和端口
    client_ip = "192.9.191.213"
    client_port = 7890

    t1 = threading.Thread(target=recv_msg, args=(server_udp_socket,))
    t2 = threading.Thread(target=send_msg, args=(server_udp_socket,client_ip,client_port))

    t1.start()
    t2.start()

    #关闭套接字



if __name__ == "__main__":
    main()