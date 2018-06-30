# Author: wangfang
#（1）判断闰年
'''
def judgeLeapYear(year):
    if (year % 4 == 0  and year % 100 != 0) or year % 400 == 0:
        print("是闰年")
    else:
        print("不是闰年")

year = int(input("请输入年份："))
judgeLeapYear(year)
'''
#（2）用函数实现输入某年某月某日，判断这一天是这一年的第几天？闰年情况也考虑进去
def outputDay(date):
    """用函数实现输入某年某月某日，判断这一天是这一年的第几天？闰年情况也考虑进去"""

    #把用户的输入年月日进行切片,转成年月日数字
    year = int(date[0:4])
    mouth = int(date[4:6])
    day = int(date[-2:])
    #定义列表，保存各个月份的天数
    mouth_day = [31,28,31,30,31,30,31,31,30,31,30,31]
    #定义统计天数的变量
    days = day
    #判断闰年，如果是闰年修改第二个月的天数为29
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        mouth_day[1] = 29
    #print(year,mouth,day)

    #计算这一天是这年的第几天
    count =  0
    while count < mouth -1:
        days = days + mouth_day[count]
        count += 1
    print(days)

#等待用户输入
date = input("请输入年月日：例如（20170101）")
outputDay(date)