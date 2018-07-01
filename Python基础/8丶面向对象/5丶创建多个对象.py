# Author: wangfang

class Cat:      #python建议类名使用大坨峰或小驼峰
    #定义方法
    def eat(self):
        print("猫在吃鱼...")
    def drink(self):
        print("猫正在喝水...")

    def introduce(self):
        print("%s的年龄是%d" % (tom_cat.name, tom_cat.age))
#创建一个叫tom_cat对象
tom_cat = Cat()  #Cat()就是根据Cat类创建一个新的对象（额外开辟一个内存空间），同时tom_cat变量指向Cat()对象的内存空间地址

#创建一个叫blue_cat对象
blue_cat = Cat()

#查看两个对象的内存地址
print(tom_cat)
print(blue_cat)

#总结：根据同一个类创建的对象的内存地址也是不同的

