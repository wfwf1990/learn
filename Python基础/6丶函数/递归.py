# Author: wangfang

'''递归'''

'''
5! = 5*4*3*2*1
4! = 4*3*2*1

5! = 5 * 4!
4! = 4 * 3!
'''

#（1）while循环实现递归方式一：
'''
num = 1
result = 1
while num <= 5:
    result = result * num
    num += 1 
print(result)
'''
#（2）函数实现递归
def test(num):
    if num > 1:
        return num * test(num - 1)
    else:
        return 1
res = test(5)
print(res)

#注意：函数递归实现是把不断调用函数叠加到内存中,如果不设置一个临界点，会造成内存溢出
#例如安卓系统一个程序会闪屏退出，这就是操作系统把内存溢出的程序杀死

