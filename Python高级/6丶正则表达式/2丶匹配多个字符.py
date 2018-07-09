# Author: wangfang

"""
*	    匹配前一个字符出现0次或者无限次，即可有可无
+	    匹配前一个字符出现1次或者无限次，即至少有1次
?	    匹配前一个字符出现1次或者0次，即要么有1次，要么没有
{m}	    匹配前一个字符出现m次
{m,n}	匹配前一个字符出现从m到n次
.*      匹配一行,除了\n换行符   如果想匹配包括\n
"""


#例：判断变量名是否有效
import re
def main():
    names = ["name1", "_name", "2_name", "__name__","2name!"]
    for temp in names:
        ret = re.match("^[a-zA-Z0-9][a-zA-Z0-9_]*$", temp)
        if ret:
            print("字符串合法:%s" % temp)
        else:
            print("字符串不合法:%s" % temp)

if __name__ == "__main__":
    main()
#总结：需要同时判断变量名的开头和结尾
#match自带判断开头,不判断结尾

