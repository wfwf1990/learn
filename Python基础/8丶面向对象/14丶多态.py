class F1(object):
    def show(self):
        print("F1.show")

class S1(F1):
    def show(self):
        print("S1.show")

class S2(F1):
    def show(self):
        print("S2.show")

#为了让Func函数既可以执行S1对象的show方法，又可以执行S2对象的show方法，所以，定义了一个S1和S2类的父类
#而实际传入的参数是：S1对象和S2对象
#函数可以根据传入对象的不同，执行对象的不同方法
def func(temp):
    temp.show()

s1_temp = S1()
s2_temp = S2()

func(s1_temp)