# Author: wangfang
oldFileName = input("请输入要拷贝的文件名字:")

oldFile = open(oldFileName,"r")

#文件存在，会执行以下动作
if oldFile:
    #获取.的下标位置
    fileFlagNum = oldFileName.rfind(".")   #

    #组织新的文件名字
    newFileName = oldFileName[:fileFlagNum] + "[复件]" + oldFileName[fileFlagNum:]

    #创建新文件
    newFile = open(newFileName,"w")

    #把旧文件的数据一行一行的进行复制到新文件中
    for line in oldFile:
        newFile.write(line)

    #把旧文件的数据一次性读取到内存中，然后在复制到新文件中
    #allLine = oldFile.read()
    #newFile.write(allLine)

    #关闭文件
    newFile.close()
    oldFile.close()
