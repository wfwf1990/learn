# Author: wangfang

#（1）可迭代对象定义：可以通过for循环这类语句迭代读取一条数据供我们使用的对象
#（2）判断一个对象是否可以迭代
#可以使用collections模块中isinstance()方法判断一个对象是否是iterable对象
'''
from collections import  Iterable
print(isinstance([],Iterable))  #是可迭代对象返回True,反之False
print(isinstance(123,Iterable))
'''


#（3）可迭代对象的本质
'''
  通过for循环遍历可迭代对象每一个元素，实际是通过迭代器实现
  在可迭代对象中的类定义了一个__inter__方法，这个方法返回的是一个迭代器
  也就是说一个具备__iter__方法的对象，就是可迭代对象
'''
'''
class Mylist(object):
    def __init__(self):
        self.container = []
    def append(self,temp):
        self.container.append(temp)
    def __iter__(self):
        """返回一个迭代器，这里先忽略"""
        pass

mylist = Mylist()
from collections import Iterable
print(isinstance(mylist,Iterable))
'''
#总结：一个对象有__iter__方法就是可迭代对象

#（5）iter()函数与next()函数
#list丶tuple等都是可迭代对象，可以通过iter()函数获取这些可迭代对象的迭代器
#然后我们可以对获取到的迭代器不断使用next()函数来获取下一个数据
#iter()函数实际上就是调用了可迭代对象的__iter__方法
'''
li = [11,22,33,44,55]
li_iter = iter(li)      #通过iter(可迭代对象)返回对象迭代器的引用
print(next(li_iter))    #next(对象迭代器) 获取数据
print(next(li_iter))
print(next(li_iter))
print(next(li_iter))
print(next(li_iter))
print(next(li_iter))
'''
#当我们已经迭代完最后一个数据之后，再次调用next()函数会抛出StopIteration异常
#来告诉我们所有的数据都已迭代完成,不用再执行函数next()函数了

#（6）判断一个对象是否是迭代器
from collections import Iterator
print(isinstance([],Iterator))
print(isinstance(iter("123"),Iterator)) #通过iter()方法获取可迭代对象的迭代器

#（7）迭代器 Iterator
'''
迭代器作用：帮助我们记录每次迭代访问到的位置
next(迭代器)：实际上是调用了迭代器对象的__next__对象，
同时python迭代器必须有__iter__方法,返回一个迭代器

总计：一个实现了__iter__方法和__next__方法的对象,就是迭代器
'''
'''
class Mylist(object):
    """自定义一个可迭代对象"""
    def __init__(self):
        self.list = []
    def add(self,temp):
        self.list.append(temp)
    def __iter__(self):
        return MyIterator(self)         #可迭代对象需要传入到迭代器中

class MyIterator(object):
    """自定义一个迭代器"""
    def __init__(self,obj):
        self.obj = obj
        self.num = 0
    def __iter__(self):
        pass
    def __next__(self):
        ret = self.obj.list[self.num]
        self.num += 1
        return ret

list1 = Mylist()
list1.add("老王")
list1.add("老张")

for name in list1:
    print(name)
'''
'''
import time
class Mylist(object):
    """自定义一个可迭代对象"""
    def __init__(self):
        self.list = []
    def add(self,temp):
        self.list.append(temp)
    def __iter__(self):
        return MyIterator(self)         #可迭代对象需要传入到迭代器中

class MyIterator(object):
    """自定义一个迭代器"""
    def __init__(self,obj):
        self.obj = obj
        self.num = 0
    def __iter__(self):
        pass
    def __next__(self):
        if self.num < len(self.obj.list):
            ret = self.obj.list[self.num]
            self.num += 1
            return ret
        else:
            raise StopIteration

list1 = Mylist()
list1.add("老王")
list1.add("老张")

for name in list1:
    print(name)
    time.sleep(1)
'''
'''
import time
class Mylist(object):
    """自定义一个可迭代对象"""
    def __init__(self):
        self.list = []
        self.num = 0        #定义num记录访问的位置
    def add(self,temp):
        self.list.append(temp)
    def __iter__(self):
        return self         #__iter__返回一个迭代器,这里对象就是一个迭代器，所以返回self
    def __next__(self):
        if self.num < len(self.list):
            ret = self.list[self.num]
            self.num += 1
            return ret
        else:
            raise StopIteration



list1 = Mylist()
list1.add("老王")
list1.add("老张")

for name in list1:
    print(name)
    time.sleep(1)
'''
#（8）for循环本质
'''
for item in Iterable 
本质：先通过iter()函数获取可迭代对象Iterable的迭代器，然后获取到迭代器不断
调用next()方法获取下一个值，并将其复制给item，当遇到StopIteration的异常后循环结束

'''

#（9）迭代器的应用场景
#1丶方式一：实现斐波那契数列
'''
nums = list()
a = 0
b = 1
i = 0
while i <10:
    nums.append(a)
    a,b = b,a+b
    i += 1 
for item in nums:
    print(item)
'''
#2丶方式二：迭代器实现斐波那契数列
class test1(object):
    def __init__(self,nums):
        self.nums = nums
        self.a = 0
        self.b = 1
        self.num = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.num < self.nums:
            ret = self.a
            self.a,self.b = self.b, self.a + self.b
            self.num += 1
            return ret
        else:
            raise StopIteration
feibo = test1(20)

ret1 = iter(feibo)      #返回迭代器对象，使用ret1变量接收
print(next(ret1))       #调用迭代器中的__next__方法
print(next(ret1))

for item in feibo:
    print(item)