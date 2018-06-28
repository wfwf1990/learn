
''''''
'''break和continue的作用范围只对当前的while生效'''
count = 1
while count <= 5:

    num = 1
    while num <=count:
        print("*",end="")       #打印不换行
        num += 1
        break
    print("")               #处理完while，换行
    count += 1