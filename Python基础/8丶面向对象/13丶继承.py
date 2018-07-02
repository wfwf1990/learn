#（1）单继承
'''
子类会继承父类的方法和属性

定义单继承：
    class 子类名(父类名):
'''

#（2）单继承：子类继承父类
'''
#定义父类
class Animal(object):

    def eat(self):
        print("吃...")
    def drink(self):
        print("喝...")
    def sleep(self):
        print("睡觉...")
    def run(self):
        print("跑")

#定义子类也叫基类
class Cat(Animal):          #子类名(父类名)  子类中的()要写上父类的名

    #定义子类自己独有的方法，注意子类与子类之间的方法无法相互调用，单子类可以继承父类的方法
        def catch(self):
            print("捉老鼠")
tom_cat = Cat()
tom_cat.sleep()
tom_cat.catch()
'''
#（3）子类继承父类与父类的父类
'''
#儿子继承爸爸的钱，爸爸的钱继承爷爷的钱，
class Animal(object):
    def eat(self):
        print("吃...")
    def drink(self):
        print("喝...")
    def sleep(self):
        print("睡觉...")
    def run(self):
        print("跑")

class Cat(Animal):    
    def catch(self):
        print("捉老鼠")
class PersianCat(Cat):
    def fly(self):
        print("飞...")

bosimao = PersianCat()
bosimao.sleep()
bosimao.catch()
bosimao.fly()
'''

#（4）子类重写父类方法
#子类的方法与父类的方法名字相同，那么子类会执行重写的方法，不会执行父类的方法
'''
class Animal(object):

    def eat(self):
        print("吃...")
    def drink(self):
        print("喝...")
    def sleep(self):
        print("睡觉...")
    def run(self):
        print("跑")
class Cat(Animal):
    def catch(self):
        print("捉老鼠")
class PersianCat(Cat):
    def catch(self):            #定义的方法名与父类Cat的方法名catch相同即可,这就是重写
        print("不会捉老鼠")
bosimao = PersianCat()
bosimao.catch()
'''

#（5）子类调用被重写父类的方法
'''
class Animal(object):

    def eat(self):
        print("吃...")
    def drink(self):
        print("喝...")
    def sleep(self):
        print("睡觉...")
    def run(self):
        print("跑")
class Cat(Animal):
    def catch(self):
        print("会捉老鼠")
class PersianCat(Cat):
    def catch(self):            #定义的方法名与父类Cat的方法名catch相同即可,这就是重写
        print("不会捉老鼠")
        print("进化中...")
        #Cat.catch(self)         #第一种：调用父类被重写的方法
        super().catch()         #第二种：调用父类被重写的方法
bosimao = PersianCat()
bosimao.catch()
'''

#（6）子类不会继承父类中的私有属性和私有方法，
# 如果想获取父类中的私有属性和私有方法必须要在父类中的定义一个公有方法专门获取私有方法和私有属性
#子类会继承父类的公有方法来获取父类的私有属性和私有方法
'''
#定义父类
class Dad(object):
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200       #定义私有属性
    def test1(self):
        print("test1")
    def __test2(self):          #定义私有方法
        print("__test2")
    def test3(self):             #在父类中定义一个方法用于获取私有属性和私有方法
        self.__test2()
        print(self.__num2)

class Son(Dad):         #定义子类，继承Dad父类
    pass

son1 = Son()            #创举对象
print(son1.num1)          #子类可以获取父类的公有属性
#print(son1.__num2)     #子类无法直接获取父类的私有属性
son1.test1()            #子类继承了父类的test1方法
#son1.__test2()         #子类无法继承父类的__test2私有方法

son1.test3()            #子类中继承了父类中的公有方法，该公有方法可以获取父类中的私有方法和私有属性
'''

#（7）多继承：子类继承多个父类
#子类会继承多个父类的方法
'''
#定义父类
class Father(object):
    def __init__(self):
        self.father_money = 0
    def SetFatherMoney(self,new_money):
        self.father_money = new_money
        print("father的资产是%s" %self.father_money)
    def GetFatherMoney(self):
        return self.father_money
#定义父类
class Mother(object):
    def __init__(self):
        self.mother_money = 0
    def SetMotherMoney(self,new_money):
        self.mother_money = new_money
        print("Mother的资产是%s" %self.mother_money)
    def GetMotherMoney(self):
        return self.mother_money
#定义子类
class Boby(Father,Mother):      #同时继承Father和Mother类
    def GetMoney(self):
        money = self.GetFatherMoney() + self.GetMotherMoney()
        print(money)

xiaoming = Boby()
xiaoming.SetFatherMoney(1000)
xiaoming.SetMotherMoney(20000000000)
xiaoming.GetMoney()
#xiaoming.GetMoney()
'''


#（8）多继承注意点：
#多个父类的方法相同，子类执行方法搜索路径的顺序是根据__mro__方法提供的路径;
#类名.__mro__
#建议父类之间的方法不要相同
'''
class Father(object):
    def __init__(self):
        self.father_money = 0
    def SetFatherMoney(self,new_money):
        self.father_money = new_money
        print("father的资产是%s" %self.father_money)
    def GetFatherMoney(self):
        return self.father_money
#定义父类
class Mother(object):
    def __init__(self):
        self.mother_money = 0
    def SetMotherMoney(self,new_money):
        self.mother_money = new_money
        print("Mother的资产是%s" %self.mother_money)
    def GetMotherMoney(self):
        return self.mother_money
#定义子类
class Boby(Father,Mother):      #同时继承Father和Mother类
    def GetMoney(self):
        money = self.GetFatherMoney() + self.GetMotherMoney()
        print(money)

xiaoming = Boby()
xiaoming.SetFatherMoney(1000)
xiaoming.SetMotherMoney(20000000000)
xiaoming.GetMoney()
print(Boby.__mro__)     #类名.__mro__  子类执行方法的搜索路径
#xiaoming.GetMoney()
'''