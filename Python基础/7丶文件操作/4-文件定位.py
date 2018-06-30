# Author: wangfang
#（1）tell() 获取当前读写的位置
'''
#打开一个已经存在的文件
f1 = open("file1.txt","r")
content = f1.read(3)        #读取3个字节
print(f1.tell())            #查找当前指针位置
content = f1.read()
print(f1.tell())
'''
#（2）seek() 定位到某个位置
'''
seek(offset,from) 
    offset：偏移量
    from 方向：
        0 ：表示文件开头
        1：表示当前位置
        2：表示文件末尾
'''
#把位置设置为：从文件开头偏移5个字节
'''
f1 = open("file2.txt","r")
f1.seek(5,0)        #位置偏移5个字节
print(f1.tell())
print(f1.readline())
f1.read()
f1.seek(0)      #调整指针到文件开头
print(f1.readlines())
'''
#把位置设置为：离文件末尾3字节处 ，注意文件必须以rb打开
'''
f1 = open("file2.txt","rb")  #打开一个已经存在的文件
position = f1.tell()        #查找当前位置
print(position)
f1.seek(-3,2)                #调整指针到文件末尾3字节处

position = f1.tell()
print(position)
'''