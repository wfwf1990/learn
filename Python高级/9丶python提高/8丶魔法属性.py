# Author: wangfang
#（1）__doc__ ：表示类的信息
'''
class Foo:
    """ 描述类信息，这是用于看片的神奇 """

    def func(self):
        pass
print(Foo.__doc__)      #输出描述类的信息
'''

#（2）__module__ 和 __class__
#__module__ 表示当前操作的对象在那个模块
#__class__ 表示当前操作的对象的类是什么
"""
import common
obj = common.Person()
print(obj.__module__)
print(obj.__class__)
"""

#（3）__init__ ：初始化方法，通过类创建对象时，自动触发执行
'''
class Person:
    def __init__(self, name):
        print("创建类对象，自动执行")
        self.name = name
        self.age = 18

obj = Person("WF")  # 创建类对象,自动执行类中的 __init__ 方法
'''

#(4)__del__ :当对象在内存中被释放时，自动触发执行。

#（5） __call__ ：对象后面加括号，触发执行
'''
class Foo:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        print('__call__')
        
obj = Foo()     #执行__init__
obj()           #执行__call__
'''

#（6）__dict__ ：查看类或对象中的所有属性,类的实例属性属于对象；类中的类属性和方法等属于类
'''
class Province(object):
    country = 'China'

    def __init__(self, name, count):
        self.name = name
        self.count = count

    def func(self, *args, **kwargs):
        print('func')
print(Province.__dict__)        #获取类属性
obj1 = Province("alex",11)
print(obj1.__dict__)        #获取实例对象属性
'''

#（7）__str__ :如果一个类中定义了__str__方法，那么在打印 对象 时，默认输出该方法的返回值。
'''
class Foo:
    def __str__(self):
        return 'laowang'
obj = Foo() 
print(obj)
'''