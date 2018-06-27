# Author: wangfang

'''if嵌套'''
'''
嵌套的if语句只有在前一个if语句条件成立的情况下才会去执行
'''
kicket = 1  #1表示买到票，0表示没有买到票
knife_lenth = 10 #刀的长度
if kicket == 1:
    print("有票，可以进站...")
    if knife_lenth >= 8:    #刀长度大于8cm就不允许进站
        print("未通过安检,刀过长，等待公安处理....")
    else:
        print("已通过安检....")
else:
    print("需要买票....")


'''if嵌套：判断白富美，高富帅'''

#等待用户输入，
sex = input("请输入性别(men或women):")
height = int(input("请输入身高："))
assets = int(input("请输入你的资产:"))
face_score = input("请输入你的颜值:")

#判断用户的性别
if sex == "men":
    if height >= 175 and assets >= 100000 and face_score == "帅":
        print("你是高富帅...")
    else:
        print("你是矮穷挫...")
elif sex == "women":
    if height >= 175 and assets >= 100000 and face_score == "美":
        print("你是白富美....")
    else:
        print("照照镜子....")
else:
    print("请输入正确的性别:")