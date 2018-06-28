''''''

'''break ：结束整个循环，执行while下面的代码'''

i = 1
while i <= 5:

    if i == 3:      #当i == 3结束while循环，while循环停止运行
        break
    print(i)
    i += 1
print("="*10)     #while循环结束,会执行while并行的语句

#打印1到100之间的20个偶数
num = 1
count = 0                       #定义打印打印偶数的计数器
while num <= 100:
    if num % 2 == 0:            #取余为0的就打印偶数
        print(num)
        count += 1              #打印一个偶数，计数器就+1
    if count == 20:             #当计数器为20的时候，while循环就结束
        break
    num += 1
