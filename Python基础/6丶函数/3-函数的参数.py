#函数参数：定义函数的时候，接收函数调用的数据
#定义函数，计算传入的两个值的和
def sum(num1,num2):
    result = num1 + num2
    print("%d + %d = %d" %(num1,num2,result))

n1 = int(input("请输入第一个值："))
n2 = int(input("请输入第二个值："))

sum(n1,n2)
