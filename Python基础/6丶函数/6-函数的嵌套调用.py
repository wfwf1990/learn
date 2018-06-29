'''函数的嵌套调用'''
#定义：一个函数里面调用了另外一个函数

#代码的重复利用

#定义函数：计算3个数值的和
def sum(a,b,c):
    result_sum = a + b + c
    #print("%d+%d+%d=%d" %(a,b,c,result))
    return  result_sum

#定义函数：计算上面3个数值的平均值
def avg(a1,a2,a3):
    result_avg = sum(a1,a2,a3)          #调用sum函数求出和,sum函数返回3个数值的和
    result_avg /= 3   #等于result_sum = result_sum / 3        #求和
    #print("平均值:%d" %result_avg)
    return result_avg                       #返回平均数的和

#定义函数：计算上面3个数值的平均值的平方
def squ(b1,b2,b3):
    result_squ = avg(b1,b2,b3)          #调用avg函数求平均值,avg函数又需要调用sum函数求3个数值的和，这就叫嵌套调用
    result_squ = result_squ ** result_squ
    print("平均值平方:%d" %result_squ)

#获取3个数值
n1 = int(input("请输入第一个数字:"))
n2 = int(input("请输入第二个数字:"))
n3 = int(input("请输入第三个数字:"))

#sum(n1,n2,n3)
#avg(n1,n2,n3)
squ(n1,n2,n3)