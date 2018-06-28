# Author: wangfang

import random
#提示并获取用户输入
player = int(input("请输入 0剪刀 1石头 2布："))
#让电脑出一个
#computer  = random.choice(range(1,4))
computer = random.randint(0,2)          #自动随机生成0,1,2 数字，随机取一个数字
#print(computer)
#判断用户的输入，然后显示对应的结果
#if 玩家获胜的条件:
if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
    print("赢了....可以去买奶粉了....")
#elif：玩家平局的条件
elif player == computer:
    print("平局,要不再来一局...")
else:
    print("输了，不要走，洗洗接着来，决战到天亮...")