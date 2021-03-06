# Author: wangfang

'''匹配单个字符'''

'''
.           匹配任意1个字符(除了\n)
[]          匹配[]中列举的字符,[0-9] [12345678] [12378] [1-37-8] [1-8abc] [0-9A-Za-z_]
\d          匹配数字,0到9
\D          匹配非数字,既不是数字
\s          匹配空白，既空格,tab键
\S          匹配非空白
\w          匹配单词字符,既A-Z a-z 0-9 _  同时支持中文字符 特殊字符除外
\W          匹配非单词字符
'''
import re
ret = re.match(r"速度激情[1-8]","速度激情8")        #匹配返回一个对象,没有匹配返回空
print(ret)
print(ret.group())