# Author: wangfang
import os
#注意：对文件和目录的操作需要os模块支持
#(1)文件常用操作 :删除文件，文件重命名
'''
#1）os.rename() 文件重命名
os.rename("file1.txt","dest-file1.txt")

#2）os.remove 删除文件
#os.remove("file1.txt")
'''
#(2)目录的常用操作：创建目录，获取当前工作目录,改变当前工作目录,获取目录下的所有文件,删除目录
'''
#1）os.mkdir 创建文件夹
#os.mkdir("dir1")
#2)os.getcwd 获取当前目录
print(os.getcwd())
#3)改变默认目录
#os.chdir("/root")
#4)获取目录列表下的所有文件,列表形式
path = r"C:\Users\lovebaby\PycharmProjects\learn\Python基础\7丶文件操作"
print(os.listdir(path))
#5）os.rmdir 删除目录
'''


