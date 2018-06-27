# Author: wangfang

'''while嵌套'''
'''
while 条件:
    条件满足的时候做的事情
    while 条件2:
        条件2满足的时候做的事情
'''

#打印矩形

'''
实现：
*
**
***
****
*****
'''
count = 1
while count <=5:
    star = "*"
    print(star*count)
    count = count + 1

count = 1
while count <=5:
    num = count
    while num <= count:
        star = "*"
        print(star*num)
        num +=1
    count = count + 1

count = 1
while count <= 5:

    num = 1
    while num <=count:
        print("*",end="")       #打印不换行
        num += 1
    print("")               #处理完while，换行
    count += 1

