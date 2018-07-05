# Author: wangfang
#（1）模块介绍
'''
# 系统自带模块
import os
print(os.__file__)

#安装三方模块：
#pip install pygame
# pip3 install pygame

#自己定义模块
'''
#（2）导入模块:import 模块
'''
import module_1
module_1.test1()       
#总结：执行模块方法    模块名.方法() 
'''
#（3）导入模块：from 模块 import 方法
#执行方式：方法()
'''
from module_1 import test1
test1()
'''
#（4）导入模块：from 模块 import *
#不建议使用这种方式
#把一个模块的所有内容导入到当前的命名空间
'''
from module_1 import test1
test1()
'''
#（5）as，导入模块的时候给模块起别名
#语法：import 模块 as 模块别名
#执行方法：模块别名.方法
'''
import time  as aa
aa.sleep(1)
'''
#（6）定位模块
#当你导入一个模块，python解释器对模块位置的搜索顺序是：
'''
先查找当前路径
模块搜索路径存储在system模块的sys.path变量中
import sys 
print(sys.path)
'''
#（7）模块制作
#导入自己定义的模块
#import module_1

#测试自己的模块
'''
def test1():
    print("test1")

def test2():
    print("test2")

def main():
    test1()
    test2()

if __name__ == "__main__":
    main()
'''

#（8）变量：__name__
#作用：当在模块中执行该模块的方法，__name__ 变量为结果为__main__
#当其他文件import这个模块 __name__ 变量结果为这个模块名

#（9）变量：__all__
#在一个模块中，如果模块中定义了__all__ = [方法或类或变量] 如果导入这个模块使用from 模块 import * ，
#那么只能使用__all__中定义的方法

