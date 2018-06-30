# Author: wangfang

#（1）文件写
#注意：如果文件不存在那么创建，如果存在那么就先清空，然后写入数据
#写文件默认不换行
'''
f1 = open("file1.txt","w")
f1.write("hello")
f1.write("\nhello")
f1.close()
'''
#（2）文件读 read(num)
#使用read(num)可以从文件中读取数据，num表示要从文件中读取的数据长度（单位是字节）
#如果没有传入num，那么就表示读取文件中的所有的数据
#注意：如果使用读多次，那么后面读取的数据是从上次读完后的位置开始
'''
f1 = open("file1.txt","r")
content = f1.read(5)        #读取5个字节
print(content)
print("-"*30)
content = f1.read()     #读取文件的所有内容
print(content)
f1.close()
'''
#(3)文件读 readlines()
#readlines可以按照行的方式把整个文件中的内容进行一次性读取，并且返回的是一个列表，其中每一行的数据为一个元素
'''
f1 = open("file1.txt","r")
content = f1.readlines()
print(content)
print(type(content))
i = 1
for temp in content:
    if len(temp.strip()) == 0:
        break
    print("%d:%s" %(i,temp.strip()))
    i += 1

f1.close()
'''
#（4）readline ：按行读取数据
f1 = open("file1.txt","r")
content = f1.readline()
print(content)
content = f1.readline()
print(content)