# Author: wangfang

"re高级功能：python独有"

#match：从头开始匹配
import re
#（1）search ：不会从头匹配，只要匹配到符合正则的，只会匹配一次
#需求：匹配除文章阅读的次数
ret1 = re.search("\d+","阅读次数：9999,阅读次数：9999")
print(ret1.group())

#（2）findall：只要符合正则，都会返回数据,提取数据不需要group，返回的是列表

ret2 = re.findall(r"\d+", "python = 9999, c = 7890, c++ = 12345")
print(ret2)

#（3）sub：将匹配到的数据进行替换,替换很多个
"""
#案例1：
ret3 = re.sub("\d+","998","python = 997")
print(ret3)

#正则表达式匹配到数据，则执行函数,同时将匹配到的对象作为实参传入到函数中
def add(temp):
    strNum = temp.group()
    num = int(strNum) + 1
    return str(num)

ret4 = re.sub(r"\d+", add, "python = 997")
print(ret4)
"""

#从下面的字符串中提取到文本
content = """
<div>
        <p>岗位职责：</p>
<p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>
<p><br></p>
<p>必备要求：</p>
<p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
<p>&nbsp;<br></p>
<p>技术要求：</p>
<p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>
<p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p>
<p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<br></p>
<p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p>
<p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>
<p>&nbsp;<br></p>
<p>加分项：</p>
<p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>
        </div>
"""
ret4 = re.sub("<[^>]*>|\n|&nbsp;","",content)
print(ret4)
ret5 = re.sub("<\w*?>|</\w*?>|\n|&nbsp;","",content)
print(ret5)
#（4）split ：切割 ，返回一个列表
#需求：切割字符串“info:xiaoZhang 33 shandong”
ret6 = re.split(":| ","info:xiaoZhang 33 shandong")
print(ret6)


