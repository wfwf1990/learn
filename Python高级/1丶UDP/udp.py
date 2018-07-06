# Author: wangfang


#（1）udp发送数据
'''
1丶创建客户端套接字
2丶发送/接收数据
3丶关闭套接字
'''
'''
import socket

def main():
    #1丶创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    #2丶准备接收方的地址
    dest_addr = ("192.9.191.201",8080)  #注意是元祖,ip是字符串,端口是数字

    while  True:
    #3丶从键盘获取数据
        send_data = input("请输入要发送的数据:")

        #用户退出程序
        if send_data == "exit":
            break

    #4丶发送数据到指定的电脑上的指定程序
        udp_socket.sendto(send_data.encode("utf-8"),dest_addr)

    #5丶关闭套接字
    udp_socket.close()

if __name__ == "__main__":
    main()
'''

#注意：发送数据先编码，收数据先解码，编码和解码的字符集必须相同
#（2）编码
'''
str->bytes:encode编码
bytes->str:decode解码
字符串通过编码成为字节码，字节码通过解码成为字符串。
bytes.decode(encoding="utf-8",errors="strict")
str.encode(encoding="utf-8",errors="strict")
'''

#（3）udp接收数据
'''
接收数据流程：
    1丶创建套接字
    2丶绑定本地信息（本地网卡ip和端口），一个端口只能被一个应用使用
    3丶接收数据
    4丶关闭套接字
'''
'''
import socket
def main():
    #1丶创建套接字
    socket_udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    #2丶绑定本地信息
    local_addr = ('',7788)  #ip地址和端口号,ip一般不用写，表示本机任意ip
    socket_udp.bind(local_addr)

    while True:
        # 3丶等待接收对方发送的数据
        recv_data = socket_udp.recvfrom(1024)  # 1024表示本次接收的最大字节数
        # 注意：recv_data这个变量接收过来的数据是一个元祖(接收到的数据,(发送的ip,端口))
        recv_msg = recv_data[0]  # 存储接收的数据
        recv_addr = recv_data[1]  # 存储发送方的地址信息

        # 4丶显示接收的数据
        #print(recv_data)
        # print("%s,%s" %(recv_msg.decode("utf-8"),str(recv_addr)))
        print("%s:%s" % (str(recv_addr),recv_msg.decode("gbk")))
        # 注意：这里windows发送过来的数据是二进制字节，需要decode解码,windows使用的gbk编码，所以这里需要使用gbk解码，而不是utf-8解码

    #5丶关闭套接字
    socket_udp.close()
if __name__ == "__main__":
    main()
'''

#（4）udp聊天器
'''
import socket

def send_msg(udp_socket):
    """获取数据，并将其发送给对方"""
    #1丶输入对方的ip
    send_ip = input("请输入接收方的ip:")
    #2丶输入对方的端口
    send_port = int(input("请输入接收方的端口："))
    #3丶从键盘输入数据
    send_data = input("请输入需要发送的数据:")
    #4丶发送数据
    udp_socket.sendto(send_data.encode("utf-8"), (send_ip,send_port))

def recv_msg(udp_socket):
    """接收数据并显示"""
    #1丶等待对方发送数据
    recv_data = udp_socket.recvfrom(1024)

    #2丶解码
    recv_msg = recv_data[0].decode("gbk")
    recv_addr = str(recv_data[1])

    #3丶显示接收到的数据
    print("%s:%s" %(recv_addr,recv_msg))

def print_menu():
    print("="*30)
    print("1丶发送数据".center(25))
    print("2丶接收数据".center(25))
    print("3丶退出程序".center(25))
    print("="*30)
def main():
    #1丶创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    #2丶绑定本地信息
    local_addr = ('', 7788)
    udp_socket.bind(local_addr)

    while True:
        #3丶选择功能
        print_menu()
        choice_num = int(input("你输入你的选择："))
        if choice_num == 1:
            # 2丶发送数据
            send_msg(udp_socket)
        elif choice_num == 2:
            # 3丶接收数据
            recv_msg(udp_socket)
        elif choice_num == 3:
            break
        else:
            print("退出...")
if __name__ == "__main__":
    main()
'''