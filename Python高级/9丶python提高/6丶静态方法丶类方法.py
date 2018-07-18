# Author: wangfang
#（1）类属性与实例属性：实例属性属于对象,类属性属于类
#实例属性需要通过对象来访问,类属性通过类访问
#类属性在内存中只保存一份,实例属性在每个对象中都要保存一份
#通过类创建实例对象时，如果每个对象需要具有相同名字的属性，那么就使用类属性，用一份既可
"""
class Province(object):
    # 类属性
    country = '中国'

    def __init__(self, name):
        # 实例属性
        self.name = name
# 创建一个实例对象
obj = Province('山东省')
# 直接访问实例属性
print(obj.name)
# 直接访问类属性
print(Province.country)
"""
#（2）实例方法丶静态方法和类方法
#   1丶方法包括：实例方法、静态方法和类方法，三种方法在内存中都归属于类，区别在于调用方式不同
#   2丶实例方法：由对象调用；至少一个self参数；执行实例方法时，自动将调用该方法的对象赋值给self；
#   3丶类方法：由类调用； 至少一个cls参数；执行类方法时，自动将调用该方法的类赋值给cls；
#   4丶静态方法：由类调用；无默认参数；
'''
class Foo(object):
    def __init__(self, name):
        self.name = name

    def ord_func(self):
        """ 定义实例方法，至少有一个self参数 """
        # print(self.name)
        print('实例方法')

    @classmethod
    def class_func(cls):
        """ 定义类方法，至少有一个cls参数 """
        print('类方法')

    @staticmethod
    def static_func():
        """ 定义静态方法 ，无默认参数"""
        print('静态方法')

f = Foo("中国")
f.ord_func()        #通过实例对象调用实例方法
Foo.class_func()    #通过类名调用类方法
Foo.static_func()   #通过类名调用静态方法
'''