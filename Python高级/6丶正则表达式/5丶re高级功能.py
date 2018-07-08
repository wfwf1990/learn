# Author: wangfang

"re高级功能：python独有"

#match：从头开始匹配
import re
#（1）search ：不会从头匹配，只要匹配到符合正则的，只会匹配一次
#需求：匹配除文章阅读的次数
ret1 = re.search("\d+","阅读次数：9999,阅读次数：9999")
print(ret1.group())

#（2）findall：只要符合正则，都会返回数据,提取数据不需要group，返回的是列表

#（3）sub：替换很多个

#（4）split ：切割



