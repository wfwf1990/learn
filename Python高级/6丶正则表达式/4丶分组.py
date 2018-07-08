# Author: wangfang

"""分组"""
"""
|	匹配左右任意一个表达式
(ab)	将括号中字符作为一个分组
\num	引用分组num匹配到的字符串
(?P<name>)	分组起别名
(?P=name)	引用别名为name分组匹配到的字符串
"""

import re

#实例 ： |   ()
ret1 = re.match(r"\w{4,20}@sina|163\.com", "163.com")
print(ret1.group())

#注意：|是匹配左右的任意一个表达式，\w{4,20}@sina 和 163\.com两部分 切记

ret2 = re.match(r"\w{4,20}@(163|126|qq)\.com", "test@qq.com")
print(ret2.group())

#实例：分组的特殊功能 提取区号和电话号码
ret3 = re.match(r"(\d{3,4})-?(\d{8}$)","010-12345678")
print(ret3.group())
print(ret3.group(1))        #提取区号，第一个()分组里面匹配的数据
print(ret3.group(2))        #提取电话号码,第二个()分组里面匹配的数据

#实例: \引用分组的字符串  匹配出<html>hh</html>
ret4 = re.match(r"<(\w*)>.*</\1>$","<html>hh</html>")
print(ret4.group())
ret5 = re.match(r"<([A-Za-z]*)>.*</\1>$","<html>hh</html>")
print(ret5.group())
ret6 = re.match(r"<(\w*)><(\w*)>.*</\2></\1>$","<body><html>hh</html></body>")
print(ret6.group())