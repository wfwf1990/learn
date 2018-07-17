import socket
import time
"""思路"""

"""
创建套接字
绑定端口信息
监听
主进程套接字非堵塞
创建列表，用于保存客户端套接字
while True:
    try :
        接收用户请求连接:创建连接客户端套接字  
    except: 
        说明没有用户连接
    else:
        说明有用户连接
        设置客户端套接字为非堵塞
        把客户端套接字加入到列表中
    for 客户端套接字 in 客户端套接字列表: 
        try：
            检测是否收到数据
        except:
            用户没有发数据
        else:
            用户发数据
                if 用户发不为空数据:
                    返回客户端真实数据
                else:
                    从列表中删除客户端套接字
                    
"""
client_socket_list = list()         #存储所有客户端socket
def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = ""
    server_port = 8080
    server_addr = (server_ip, server_port)

    tcp_server_socket.bind(server_addr)
    tcp_server_socket.listen(128)

    #将套接字设置为非堵塞
    # 设置为非堵塞后，如果accept时，恰巧没有客户端connect，那么accept会
    # 产生一个异常，所以需要try来进行处理
    tcp_server_socket.setblocking(False)


    while True:
        time.sleep(1)
        try:
            client_socket,client_addr = tcp_server_socket.accept()
        except Exception as ret:
            print("没有客户端连接")
        else:
            print("一个新的客户端到来%s" %client_socket)
            client_socket.setblocking(False)        #设置为非堵塞
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
                else:
                    client_socket_temp.close()
                    client_socket_list.remove(client_socket_temp)
                    print("客户端已经关闭")
if __name__ == "__main__":
    main()