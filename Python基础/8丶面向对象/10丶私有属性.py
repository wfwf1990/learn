
'''私有属性'''
'''
如果有一个对象，当需要对其进行修改属性时，有2种方法
    对象名.属性名 = 数据 ---->直接修改
    对象名.方法名() ---->间接修改
为了更好的保存属性安全，即不能随意修改，一般的处理方式为
    将属性定义为私有属性
    添加一个可以调用的方法，供调用
'''
class Person(object):
    def __init__(self,new_name):
        self.__name = new_name      #定义私有属性,如果在属性名前面加了2个下划线'__'，则表明该属性是私有属性，否则为公有属性
    def GetName(self):
        return self.__name
    def SetName(self,new_name):
        if len(new_name) >=5:
            self.__name = new_name
        else:
            print("error：名字长度需要大于或等于5")


xiaoming = Person("xiaoming")
#print(xiaoming.__name)      #私有属性无法直接获取
print(xiaoming.GetName())