# Author: wangfang
#大文件处理方式：不建议使用readlines readline read()

#1个文件如果是5G大小，使用while循环，建议使用1K读取,当读取到文件内容长度为0,说明读取到文件尾部就结束该循环
f1 = open("file1.txt","r")
while True:
    content = f1.read(1024)
    print(len(content))
    if len(content) == 0:
        break