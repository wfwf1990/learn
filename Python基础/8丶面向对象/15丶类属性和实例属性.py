'''实例属性和类属性'''

'''
实例属性：和具体的某个实例对象有关系，并且一个实例对象和另外一个实例对象是不共享属性的
类属性：类属性所属于类对象，并且多个实例对象之间共享同一个类属性
    类属性只会定义一次，不会被每次创建对象而重新定义
'''


#（1）类属性:在class中定义,def外定义就是类属性
'''
class Person(object):
    name = "tom"            #公共的类属性
    __age = 20              #私有的类属性
    def __init__(self):
        Person.address = "北京"    #每次创建对象，实例对象都会调用一次

tom = Person()
print(Person.name)          #获取类属性
print(Person.address)       #获取类属性

#print(tom.__age)        #错误，不能在类外通过实例对象访问私有的类属性
#print(Person.__age)    #错误，不能在类外通过实例对象访问私有的类属性
'''
#（2）实例属性（对象属性）
#实例属性只能通过对应的对象访问，访问类属性必须通过类对象访问
#是类对象所拥有的方法，需要用修饰器@classmethod来标识其为类方法，对于类方法，第一个参数必须是类对象，
# 一般以cls作为第一个参数（当然可以用其他名称的变量作为其第一个参数，
# 但是大部分人都习惯以'cls'作为第一个参数的名字，就最好用'cls'了），能够通过实例对象和类对象去访问。
'''
class People(object):
    address = '山东' #类属性
    def __init__(self):
        self.name = 'xiaowang' #实例属性
        self.age = 20 #实例属性
p = People()
p.age =12 #实例属性
print(p.address) #正确
print(p.name)    #正确
print(p.age)     #正确

print(People.address) #正确
#print(People.name)    #错误
#print(People.age)     #错误
'''

#（3）统计类被引用次数
'''
class test():
    num = 0         #定义类属性
    def __init__(self):
        test.num += 1       #定义类属性,根据类创建对象每次都会调用__init__方法
        #每次创建对象,test.num的类属性的值都会+1

a = test()
b = test()
c = test()
print(test.num)
'''

#（4）类方法
'''
class People(object):
    #类属性
    country = "china"

    #定义实例方法
    def __init__(self):
        self.name = "tom"

    #定义类方法，使用classmethod进行修饰
    @classmethod
    def getCountry(cls):
        return  cls.country

    @classmethod
    def setCountry(cls,new_country):
        cls.country = new_country

p = People()
print(p.getCountry())       #通过实例对象获取类属性
print(People.getCountry())  #通过类对象的类方法获取类属性

#p.setCountry("Japen")       #可以通过这个类创建出来的对象去调用这个类的方法
People.setCountry("Japen")      #可以通过类的名字调用类方法
print(p.getCountry())

'''

#（5）静态方法
#需要通过修饰器@staticmethod来进行修饰，静态方法不需要多定义参数

class  People(object):
    country = 'china'

    @staticmethod
    def getCountry():       #函数不需要任何参数
        return People.country

print(People.getCountry())      #通过类方法获取类属性