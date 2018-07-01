# Author: wangfang

'''
__init__()方法，在创建一个对象时默认被调用，不需要手动调用
__init__(self)中，默认有1个参数名字为self，如果在创建对象时传递了2个实参，那么__init__(self)中出了self作为第一个形参外还需要2个形参，例如__init__(self,x,y)
__init__(self)中的self参数，不需要开发者传递，python解释器会自动把当前的对象引用传递进去
'''
class Cat:      #python建议类名使用大坨峰或小驼峰

    #初始化对象,默认值设定,python解释器会自动调用__init__方法
    def __init__(self,new_name,new_age):
        self.name = new_name
        self.age = new_age
        self.sex = "man"        #定义默认属性，创建对象不需要传递，在方法中可以直接使用该属性
    #定义方法
    def eat(self):
        print("猫在吃鱼...")
    def drink(self):
        print("猫正在喝水...")

    def introduce(self):
        print("%s的年龄是%d" % (self.name, self.age))
#创建一个叫tom_cat对象
tom_cat = Cat("tom",10)
tom_cat.introduce()  #相当于tom_cat.introduce()

#创建一个叫blue_cat对象
blue_cat = Cat("blue",20)
blue_cat.introduce()
