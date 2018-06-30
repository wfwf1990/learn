# Author: wangfang
import os
#获取指定目录下的所有文件
path = r"C:\Users\lovebaby\PycharmProjects\learn\Python基础\7丶文件操作\dir1"
list_file = os.listdir(path)
#print(list_file)

file_flag = 0   #1表示添加标志，0标识删除标志


#循环遍历处理文件
for old_file in list_file:
    print(old_file)
    if file_flag == 1:
        old_file_name = path + "\\" + old_file
        new_file_name = path + "\\" + "[京东出品]-" + old_file
        os.rename(old_file_name,new_file_name)
    elif file_flag == 0:
        nums = len("[京东出品]-")
        old_file_name = path + "\\" + old_file
        new_file_name = path + "\\" + old_file[nums:]
        os.rename(old_file_name,new_file_name)
