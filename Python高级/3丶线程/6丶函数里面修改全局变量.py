# Author: wangfang
num1 = 100
num2 = [10,20]

def test1():
    global num1
    num1 += 100

def test2():
    num2.append(30)

print(num1)
print(num2)

test1()
test2()

print(num1)
print(num2)

#总结：如果全局变量是可变类型，函数中修改全局变量是不需要加global选项
#如果全局变量是不可变类型，函数中修改全局变量是需要加blobal选项

