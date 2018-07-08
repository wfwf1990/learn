# Author: wangfang

'''开头结尾'''
'''
^	匹配字符串开头
$	匹配字符串结尾
\   转义字符，让有意义的字符变成初始状态
'''

#例:匹配出163的邮箱地址，且@符号之前有4到20位，例如hello@163.com
import re
def main():
    email_list = ["xiaoWang@163.com", "xiaoWang@163.comheihei", ".com.xiaowang@qq.com"]
    for temp in email_list:

        #如果在正则表达式中需要用到了某些普通的字符,比如 .或?等,仅仅需要在他们前面添加一个反斜杠转义
        ret = re.match("\w{4,20}@163\.com$",temp)
        if ret:
            print("合法的邮箱是:%s" %temp)
        else:
            print("不合法的邮箱是:%s" %temp)

if __name__ == "__main__":
    main()

#注意：要判断邮箱的开头和结尾, xiaoWang@163.comheihei   注意这种邮箱地址
# .com这里的.表示匹配任意一个字符,需要使用\转义字符
