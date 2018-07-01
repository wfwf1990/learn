# Author: wangfang
#（1）创建对象格式
'''
对象名 = 类名()
'''

#（2）demo：创建对象
#第一个Cat类
class Cat:      #python建议类名使用大坨峰或小驼峰
    #定义方法
    def eat(self):
        print("猫在吃鱼...")
    def drink(self):
        print("猫正在喝水")

#创建一个对象
tom_cat = Cat()  #Cat()就是根据Cat类创建一个新的对象（额外开辟一个内存空间），同时tom_cat变量指向Cat()对象的内存空间地址
print(tom_cat)