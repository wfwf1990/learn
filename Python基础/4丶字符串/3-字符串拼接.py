'''字符串拼接两种方式'''


'''方式一'''
#使用+符号进行字符串的拼接
str1 = "lao"
str2 = "wang"
str3 = str1 + str2
print(str3)
'''
运行结果：laowang
'''
#注意：使用+符号，python会判断数据类型，如果是字符串会进行字符串的拼接，如果是数字类型会进行算法运算
num1 = 100
num2 = 200
sum = num1 + num2
print(sum)

'''方式二'''
#使用格式化符号%s
str4 = "lao"
str5 = "wang"
str6 = "===%s==="%(str4 + str5)
print(str6)