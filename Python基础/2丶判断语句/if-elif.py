''''''
#多个条件判断
'''

if 条件1:
    语句1
elif 条件2:
    语句2
elif 条件3:
    语句3
else 条件4:           #可有可无
    语句4 
注意：只要任何条件满足，不会执行下面的条件
'''


#获取用户输入的数据
num = int(input("请输入数字(1-7):"))

#判断用户输入的数据
if num == 1:
    print("星期一")
elif num == 2:
    print("星期二")
elif num == 3:
    print("星期三")
elif num == 4:
    print("星期四")
elif num == 5:
    print("星期五")
elif num == 6:
    print("星期六")
elif num == 7:
    print("星期日")
else:
    print("你输入的信息有误！")