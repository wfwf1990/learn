# Author: wangfang
#（1）property属性
#   1丶定义：使用的实例属性一样的特殊属性，可以对应于某个方法
"""
# ############### 定义 ###############
class Foo:
    def func(self):
        pass

    # 定义property属性
    @property
    def prop(self):
        return 123
foo_obj = Foo()
foo_obj.func()      #调用实例方法
ret = foo_obj.prop        #调用property属性
print(ret)
"""
#   2丶property属性的定义和调用要注意一下几点：
    #定义时，在实例方法的基础上添加 @property 装饰器；并且仅有一个self参数
    #调用时，无需括号
        #方法：foo_obj.func()
        #property属性：foo_obj.prop
#（2）简单的实例
"""
对于京东商城中显示电脑主机的列表页面，每次请求不可能把数据库中的所有内容都显示到页面上，而是通过分页的功能局部显示，所以在向数据库中请求数据时就要显示的指定获取从第m条到第n条的所有数据 这个分页的功能包括：
根据用户请求的当前页和总数据条数计算出 m 和 n
根据m 和 n 去数据库中请求数据

"""
# ############### 定义 ###############
"""
class Pager:
    def __init__(self, current_page):
        # 用户当前请求的页码（第一页、第二页...）
        self.current_page = current_page
        # 每页默认显示10条数据
        self.per_items = 10

    @property
    def start(self):
        val = (self.current_page - 1) * self.per_items
        return val

    @property
    def end(self):
        val = self.current_page * self.per_items
        return val
p = Pager(1)
ret1 = p.start
ret2 = p.end
print(ret1)
print(ret2)
"""
#（3）property属性的两种方式
"""
装饰器 即：在方法上应用装饰器
类属性 即：在类中定义值为property对象的类属性
"""
#（4）装饰器方式实现property属性:在类的实例方法上应用@property装饰器
#3丶1经典类，具有一种@property装饰器
"""
class Person(object):
# ############### 定义 ###############
    @property
    def getValue(self):
        return 123

# ############### 调用 ###############
god1 = Person()
ret = god1.getValue #自动执行@property修饰的getValue方法，并获取方法的返回值
print(ret)
"""

#3丶2新式类：具有三种@property装饰器
#由于新式类中具有三种访问方式，我们可以根据它们几个属性的访问特点，分别将三个方法定义为对同一个属性：获取、修改、删除
'''
#coding=utf-8
# ############### 定义 ###############
class Goods:
    """python3中默认继承object类
        以python2、3执行此程序的结果不同，因为只有在python3中才有@xxx.setter  @xxx.deleter
    """
    @property
    def price(self):
        print('@property')

    @price.setter
    def price(self, value):
        print('@price.setter')

    @price.deleter
    def price(self):
        print('@price.deleter')
# ############### 调用 ###############
obj = Goods()
obj.price       #自动执行 @property 修饰的 price 方法，并获取方法的返回值
obj.price = 100 #自动执行 @price.setter 修饰的 price 方法，并将  123 赋值给方法的参数
del obj.price   ## 自动执行 @price.deleter 修饰的 price 方法
'''
'''
class Goods(object):

    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    @property
    def price(self):
        # 实际价格 = 原价 * 折扣
        new_price = self.original_price * self.discount
        return new_price

    @price.setter
    def price(self, value):
        self.original_price = value

    @price.deleter
    def price(self):
        del self.original_price
obj = Goods()
print(obj.price)        #获取商品价格
obj.price = 1000        #修改商品价格
print(obj.price)
del obj.price           #删除商品原价
'''
#（5）类属性方式：当使用类属性的方式创建property属性时，经典类和新式类无区别

'''

class Foo:
    def get_bar(self):
        return 'laowang'

    BAR = property(get_bar)
obj = Foo()
ret = obj.BAR      #自动调用get_bar方法，并获取方法的返回值
'''
"""
property方法中有个四个参数

第一个参数是方法名，调用 对象.属性 时自动触发执行方法
第二个参数是方法名，调用 对象.属性 ＝ XXX 时自动触发执行方法
第三个参数是方法名，调用 del 对象.属性 时自动触发执行方法
第四个参数是字符串，调用 对象.属性.__doc__ ，此参数是该属性的描述信息
"""
'''
#coding=utf-8
class Foo(object):
    def get_bar(self):
        print("    getter...")
        return 'laowang'

    def set_bar(self, value):
        """必须两个参数"""
        print("setter...")
        return 'set value' + value

    def del_bar(self):
        print("deleter...")
        return 'laowang'

    BAR = property(get_bar, set_bar, del_bar, "description...")

obj = Foo()
ret = obj.BAR   # 自动调用第一个参数中定义的方法：get_bar
print(ret)
obj.BAR = "wangfang"    #自动调用第二个参数中定义的方法：set_bar方法，并将"wangfang"当做参数传入
desc = Foo.BAR.__doc__  #自动获取第四个参数中设置的值
print(desc)
del obj.BAR             #自动调用第三个参数中的定义的方法：del_bar方法
'''
#通过使用property属性，能够简化调用者在获取数据的流程

#（6）私有属性添加getter和setter方法
'''
class Money(object):
    def __init__(self):
        self.__money = 0

    def getMoney(self):
        return self.__money

    def setMoney(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print("error:不是整型数字")
obj_m = Money()
obj_m.setMoney(-1)
print(obj_m.getMoney())
'''

#（7）使用property升级getter和setter方法
'''
class Money(object):
    def __init__(self):
        self.__money = 0

    def getMoney(self):
        return self.__money

    def setMoney(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print("error:不是整型数字")

    # 定义一个属性，当对这个money设置值时调用setMoney,当获取值时调用getMoney
    money = property(getMoney, setMoney)

obj_m = Money()
obj_m.money = 100   #调用setMoney方法
print(obj_m.money)  #调用getMoney方法
'''

#（8）使用property取代getter和setter方法
'''
class Money(object):
    def __init__(self):
        self.__money = 0

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print("error:不是整型数字")
obj_m = Money()
obj_m.money = 100
print(obj_m.money)
'''