

print(range(10))            #在for循环中使用，range生成一个列表，这里表示生成0到9的数字列表
for temp in range(10):
    print(temp)
range(1,10)                 #生成1到9数字列表
range(1,10,2)               #步长为2


#基本方式
ret = [temp for temp in range(1,10)]
print(ret)

#在循环中嵌套if语句

ret = [temp for temp in range(1,10) if temp % 2 == 0]
print(ret)

#在循环中嵌套for循环
ret = [i for i in range(3) for k in range(2)]
print(ret)
ret = [(i,k) for i in range(3) for k in range(2)]
print(ret)

#相当于
list1 = []
for i in range(3):
    for j in range(2):
        list1.append((i,j))
print(list1)