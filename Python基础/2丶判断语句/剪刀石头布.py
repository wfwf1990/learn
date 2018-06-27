# Author: wangfang

import random


#提示并获取用户输入
player = int(input("请输入 0剪刀 1石头 2布："))

#让电脑出一个
computer  = random.choice(range(1,4))

#判断用户的输入，然后显示对应的结果
if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
    print("赢了....可以去买奶粉了....")
