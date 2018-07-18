# Author: wangfang
"""模块导入方式"""
"""
import 模块名
from 模块名 import * 
from 模块名 import 类1，类2
from 模块名 import 方法1 as 新变量
"""
#2丶模块搜索路径  ：从上面列出的目录里依次查找要导入的模块文件 ，优先从当前路径
import sys
print(sys.path)
#3丶添加新的模块路径
#方式一：sys.path.append(r"C:\Users\lovebaby\PycharmProjects\learn\Python高级\8丶多任务web服务器")
#方式二：sys.path.insert(0,r"C:\Users\lovebaby\PycharmProjects\learn\Python高级\8丶多任务web服务器")

#4丶重新导入模块
#模块被导入后，如果模块的内容修改了，需要重新导入模块
"""
from imp import reload
reload(模块名)
"""