# Author: wangfang
#(1)__new__方法
'''
class A(object):
    def __init__(self):
        pass
    def __new__(cls, *args, **kwargs):
        print("这是一个自动创建对象的方法")
        return object.__new__(cls)

a1 = A()
#A()  先执行__new__方法创建对象,然后找到一个变量接收这个对象的引用
#然后执行init方法，进行初始化对象，最后返回对象的引用
'''
#(2)创建单例对象：创建多个对象指向同一个内存地址
'''
class A(object):
    __intance = None        #定义一个类属性
    def __init__(self):
        pass
    def __new__(cls, *args, **kwargs):
        print("这是一个自动创建对象的方法")
        if cls.__intance == None:
            cls.__intance = object.__new__(cls)
            return cls.__intance
        else:
            return cls.__intance

a1 = A()    #第一次创建对象，把对象的引用返回给cls.__intance
a2 = A()    #第二次创建对象由于cls.__intance类属性不为空，直接返回cls.__intance对象的引用
print(id(a1))
print(id(a2))
'''

#（3）只初始化一次对象
class A(object):
    __intance = None        #定义一个类属性
    __value = False
    def __new__(cls, name):
        print("这是一个自动创建对象的方法")
        if cls.__intance == None:
            cls.__intance = object.__new__(cls)
            return cls.__intance
        else:
            return cls.__intance

    def __init__(self,name):
        if A.__value == False:
            self.name = name
            A.__value = True


a1 = A("小狗")    #第一次创建对象，把对象的引用返回给cls.__intance
print(a1.name)
a2 = A("大狗")    #第二次创建对象由于cls.__intance类属性不为空，直接返回cls.__intance对象的引用
print(a2.name)
print(id(a1))
print(id(a2))

