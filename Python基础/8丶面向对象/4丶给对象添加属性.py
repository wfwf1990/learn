# Author: wangfang

class Cat:      #python建议类名使用大坨峰或小驼峰
    #定义方法
    def eat(self):
        print("猫在吃鱼...")
    def drink(self):
        print("猫正在喝水...")

    def introduce(self):
        print("%s的年龄是%d" % (tom_cat.name, tom_cat.age))
#创建一个对象
tom_cat = Cat()  #Cat()就是根据Cat类创建一个新的对象（额外开辟一个内存空间），同时tom_cat变量指向Cat()对象的内存空间地址
print(tom_cat)

#调用对象的方法
tom_cat.eat()
tom_cat.drink()

#给tom指向对象添加两个属性（属性就是变量）
tom_cat.name = "汤姆"
tom_cat.age = 18

#获取对象的属性
tom_cat.introduce()