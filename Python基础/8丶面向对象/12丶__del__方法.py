'''__del__方法'''
'''
创建对象后python解释器会默认调用__init__()方法
当删除一个对象时,python解释器会默认调用一个__del__()方法
'''

'''
当有1个变量保存了对象的引用时，此对象的引用计数就会加1
当使用del删除变量指向的对象时，如果对象的引用计数不为1，比如3，那么此时只会让这个引用计数减1，
    即变为2，当再次调用del时，变为1，如果再调用1次del，此时会真的把对象进行删除
'''
#（1）del方法
#同一个类创建的所有对象删除之后，才会执行del方法
#对象没有全部删除，程序退出的时候也会自动执行del方法
'''
class Animal(object):
    def __init__(self,new_name):
        self.name = new_name

    def __del__(self):
        print("__del__方法被调用！")

dog1 = Animal("dog")
dog2 = dog1
dog3 = dog1

del dog1
print("="*50)
'''

#（2）测量对象的引用个数
#使用sys模块的getrefcount方法获取对象的引用个数，返回值比实际多出1个1
'''
import sys
class Animal(object):
    def __init__(self,new_name):
        self.name = new_name

    def __del__(self):
        print("__del__方法被调用！")

dog1 = Animal("dog")
print(sys.getrefcount(dog1))        #测试对象被引用的个数，这里结果是2，实际是1，还有1个是被方法sys方法使用
dog2 = dog1
print(sys.getrefcount(dog1))
dog3 = dog1
print(sys.getrefcount(dog1))
'''