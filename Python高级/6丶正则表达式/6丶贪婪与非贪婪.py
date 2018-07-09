# Author: wangfang

#python中使用正则表达式默认是贪婪模式
import re
s="This is a number 234-235-22-423"
#这种情况是贪婪
ret = re.match("(.*)(\d+-\d+-\d+-\d+)",s)
print(ret.group(1))
print(ret.group(2))

#去掉贪婪：在"*","?","+","{m,n}"后面加上？，使贪婪变成非贪婪。
ret = re.match("(.*?)(\d+-\d+-\d+-\d+)",s)
print(ret.group(1))
print(ret.group(2))


#提取字符串：
s = """
<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" style="display: inline;">
"""
ret = re.findall("https://.*\.jpg",s)           #贪婪
print(ret)
ret = re.findall("https://.*?\.jpg",s)          #去除贪婪
print(ret)