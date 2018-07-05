#（1）包
#一个.py文件就是一个模块，如果一个目录下有多个.py文件和__init__.py文件，那么这个目录就叫做包

#1丶在msg目录下的__init__文件中，from . import sendmsg 表示从当前目录导入sendmsg模块
#在这个文件中，导入msg包，使用包中的模块的方法
'''
import msg
msg.sendmsg.sendMsg()
'''

#2丶在在msg目录下的__init__文件中，定义__all__ = ["sendmsg"]  使用from msg(包) import * 方式表示导入msg包下指定的sendmsg模块
'''
from msg import * 
sendmsg.sendMsg()
'''

#3丶总结
#__init__.py 为空 ，仅仅是把这个包导入，不会导入包中的模块
#__all__ 变量，它控制着from 包名 import * 导入的模块
