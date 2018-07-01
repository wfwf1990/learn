# Author: wangfang

#（1）默认没有__str__方法
#print(对象) 返回的是对象的内存地址
'''
class Cat:      #python建议类名使用大坨峰或小驼峰

    #初始化对象,默认值设定,python解释器会自动调用__init__方法
    def __init__(self,new_name,new_age):
        self.name = new_name
        self.age = new_age

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
print(tom_cat)
'''
#（2）有__str__方法
class Cat:      #python建议类名使用大坨峰或小驼峰

    #初始化对象,默认值设定,python解释器会自动调用__init__方法
    def __init__(self,new_name,new_age):
        self.name = new_name
        self.age = new_age
    def __str__(self):
        msg = "%s的年龄是%d" %(self.name,self.age)
        return msg
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
print(tom_cat)          #接收__str__方法的返回值的值
