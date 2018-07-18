# Author: wangfang
"""私有化"""

"""
XX      #共有变量
_XX     #单前置下划线,私有化属性或方法,from somemodule import *禁止导入,类对象和子类可以访问,_名的变量、函数、类在使用from xxx import *时都不会被导入
__xx    #双前置下划线,父类中属性名为__名字的，子类不继承，子类不能访问,如果在子类中向__名字赋值，那么会在子类中定义的一个与父类相同名字的属性
__xx__  #双前后下划线,用户名字空间的魔法对象或属性
xx_     #单后置下划线,用于避免与Python关键词的冲突
"""
class Person(object):
    def __init__(self,name):
        self.name = name
        self._age = 20
        self.__sex = "boy"
class Student(Person):
    def getSex(self):
        self.__sex = "girl"
        return self.__sex

laowang = Student("laowang")
print(laowang.name)
print(laowang._age)
#print(laowang.__sex)
print(laowang.getSex())