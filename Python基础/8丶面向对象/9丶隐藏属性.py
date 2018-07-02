#类中的属性建议使用通过方法获取，如果传递一个属性的值不合法，那么通过方法对值进行二次修改


#通过方法设置和获取属性，就可以在方法中进行数据合法性的检查
class Dog(object):
    def SetAge(self,new_age):
        if new_age >=0 and new_age <= 100:
            self.age = new_age
        else:
            self.age = 0
    def GetAge(self):
        return self.age

dog1 = Dog()
dog1.SetAge(-10)        #例如这里传入的值是-10 
res = dog1.GetAge()
print(res)
