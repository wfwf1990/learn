# Author: wangfang
''''''
#（1）局部变量：局部变量只在定义的函数里面生效，以外都不生效
'''
def test1():
    a = 100         #定义局部变量，只在当前函数里面生效
def test2():
    print("a = %d" %a)  #想调用test1()函数里面的变量a 这是无法实现的,因为a是另外一个函数的局部变量

test1()
#test2()
'''
#（2）全局变量：函数外定义的变量，可以在函数里面使用
'''
函数内如果引用了变量，先查找函数里面有没有定义了局部变量， 
如果函数内没有局部变量，在去函数外面查找有没有定义了全局变量
'''
#(3)一个函数想使用其它函数定义的局部变量
'''
def getTem():
    tem = 33
    return tem
def printTem(tem):
    print("现在温度是%d" %tem)

res = getTem()    #使用res变量接收getTem函数的返回值
printTem(res)     #把res变量的值传入到当前函数中
'''
#（4）定义全局变量，在函数中修改全局变量的值，在其它函数中调用该全局变量修改的结果
'''
#定义一个全局变量,初始值为0     
tem = 0
def getTem():
    #tem = 33  #如果tem这个变量已经在全局变量的位置定义了,此时还想在函数中对这个全局变量进行修改的话，那么仅仅
    #定义是tem= 33 一个值这还不够，此时tem这个变量是局部变量，仅仅是和全局变量的名字相同罢了
    global tem    #声明tem变量为全局变量，那么这个函数中的tem = 33就不是一定一个局部变量，而是对全局变量做修改
    tem = 33   #
def printTem():
    print("现在温度是%d" %tem)
getTem()
printTem()
'''
#（5）全局变量定义注意点：引用全局变量必须在调用函数之前就定义了全局变量
'''
#建议把全局变量定义在定义函数之前
a = 100
def test1():
    print("a=%d" %a)
    print("b=%d" %b)
    print("c=%c" %c)
b = 200
test1()
c = 300             #这个全局变量是在test1()函数调用之后定义的
'''
'''
a = 100 
b = 200 
c = 300 
def test1():
    print("a=%d" %a)
    print("b=%d" %b)
    print("c=%c" %c)
'''
#（6）全局变量和局部变量名字相同
'''
a = 100
def test1():
    a = 200 #在函数中，如果对一个和全局变量名相同的变量进行=value的时候，默认是定义一个变量
            #只不过这个变量的名字和全局变量的名字相同罢了
            #如果想在执行a=value时候，不是定义局部变量，而是对全局变量进行修改，那么可以添加global进行声明
    print("a=%d"%a)
def test2():
    print("a=%d"%a) #如果这里打印了100，就说明了test1函数没有对全局变量做修改，而是定义了一个局部变量
test1()
test2()
'''
#（7）全局变量命令-建议
'''
g_a = 100 
def test():
    a = 100 
'''



