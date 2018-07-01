# Author: wangfang
#self 那个对象调用self，那么self就是这个对象
'''
class Cat:      #python建议类名使用大坨峰或小驼峰
    #定义方法
    def eat(self):
        print("猫在吃鱼...")
    def drink(self):
        print("猫正在喝水...")

    def introduce(self):
        print("%s的年龄是%d" % (self.name, self.age))
#创建一个叫tom_cat对象
tom_cat = Cat()
tom_cat.name = "tom"
tom_cat.age = 20
tom_cat.introduce()  #相当于tom_cat.introduce()

#创建一个叫blue_cat对象
blue_cat = Cat()
blue_cat.name = "blue"
blue_cat.age = 30
blue_cat.introduce()

'''
#注意：类中的方法必须至少有1个参数，一般名字叫做self,
#表示当调用对象的方式时把这个对象给传入到方法中
