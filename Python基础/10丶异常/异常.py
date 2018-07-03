# Author: wangfang
#（1）异常
#程序出现异常，python解释器无法往下继续执行

#（2）异常处理
'''
try:
    print(num)
    print("---------1-----------")
except NameError:
    print("接收到异常的处理....")
print("----------2----------")
'''
#总结：
#try中的代码如果出现异常,那么异常下面的代码都不会执行
#except如果捕获到try中的异常，会执行except里面的代码，如果没有捕获到，整个出现崩溃

#（3）except处理多个指定类型异常
'''
try:
    #print(num)
    open("test.txt")
except (NameError,FileNotFoundError):
    print("程序出现异常..")
'''

#（4）多个except处理指定类型异常
'''
try:
    #print(num)
    open("test.txt")
except NameError:
    print("变量没有定义...")
except FileNotFoundError:
    print("文件不存在")
'''
#（5）except捕获所有异常类型
'''
try:
    #print(num)
    open("test.txt")
except Exception:
    print("Exception是所有异常的父类,捕获所有的异常")
'''
#（6）except ... as 变量名
#被捕获的异常作为值赋予一个变量
'''
try:
    #print(num)
    open("test.txt")
except Exception as e :
    print(e)
'''
#（7）else 没有异常才会执行
'''
try:
    #print(num)
    #open("test.txt")
    print("------1---------")
except Exception as e :
    print(e)
else:
    print("没有异常才会执行")
'''
#（8）finally ：不管有没有异常都会执行
'''
try:
    #print(num)
    #open("test.txt")
    print("------1---------")
except Exception as e :
    print(e)
else:
    print("没有异常才会执行")
finally:
    print("不管有没有异常都会执行")
'''
#（9）try嵌套
'''
try:
    f = open("test.txt")
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
    except:    #如果在读取文件过程中，产生了异常，那么就会捕获到，例如ctrl+c
        pass
    finally:
        f.close()       #不管有没有异常，文件都要被关闭
except:
    print("文件不存在...")
'''

#（10）异常的传递，异常在函数中传递
'''
def test1():
    print("----------test1-1---------")
    print(num)
    print("----------test1-2---------")
def test2():
    print("----------test2-1---------")
    test1()
    print("----------test2-2---------")
def test3():
    try:
        print("----------test3-1---------")
        test2()
        print("----------test3-2---------")
    except Exception as result:
        print("捕获到了异常，异常是%s" %result)

test3()
'''

#（11）抛出自定义异常
'''
#定义一个异常类
class ShortInputException(Exception):
    def __init__(self,length,atleast):
        self.length = length
        self.atleast = atleast

def main():
    try:
        s = input("请输入一个字符串:")
        if len(s) < 3:
            raise ShortInputException(len(s),3)     #出现异常,返回一个对象
    except ShortInputException as result:       #result作为变量指向这个对象
        print("ShortInputException:输入的长度是%d,长度最少是%d" %(result.length,result.atleast))
        
if __name__ == '__main__':
    main()
'''

#（12）异常处理中抛出异常
'''
class Test(object):
    def __init__(self,new_value):
        self.value = new_value
    def Cal(self,num1,num2):
        try:
            return  num1/num2
        except Exception as result:
            if self.value == True:
                print("程序出现异常：%s" %result)
            else:
                raise
A = Test(True)
A.Cal(1,0)
B = Test(False)
B.Cal(1,0)
'''