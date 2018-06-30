# Author: wangfang
#（1）方式一
a = 4
b = 5

c = a
a = b
b = c
print("a=%d\nb=%d" %(a,b))

#（2）方式二：
a = 4
b = 5
a = a + b
b = a - b
a = a - b
print("a=%d\nb=%d" %(a,b))

#（3）方式三：
a = 4
b = 5
a,b = b,a
print("a=%d\nb=%d" %(a,b))