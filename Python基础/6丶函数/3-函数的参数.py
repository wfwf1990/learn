#函数参数：定义函数的时候，接收函数调用的数据
#（1）传递参数：定义函数，计算传入的两个值的和
'''
def sum(num1,num2):
    result = num1 + num2
    print("%d + %d = %d" %(num1,num2,result))

n1 = int(input("请输入第一个值："))
n2 = int(input("请输入第二个值："))

sum(n1,n2)
'''

#（2）缺省参数：函数调用的时候没有传入实际参数，函数使用默认值，如果调用函数传递了参数，则不使用缺省参数
#注意：缺省参数需要定义在最后
'''
def test1(a,b,c=33):
    print(a)
    print(b)
    print(c)
test1(11,22)    #定义函数时有3个形参，而调用函数只传入2个实际参数，如果函数定义有默认参数，则使用默认值
test1(11,22,44) #如果定义函数有默认值，调用函数也传入了值，则使用调用函数的实际参数
'''

#（3）命名参数:调用函数指定了参数(变量名=值),同时变量名与定义函数时的参数变量名相同
'''
def test1(a,b,c=33):
    print(a)
    print(b)
    print(c)
test1(11,b=44,c=55)  #函数调用指定了b=44,c=55,同形参的变量名相同,这种就叫做命名参数
'''

#总结：调用函数传递参数的个数必须与定义函数个数数量相同（除了定义了缺省参数除外）


#（3）不定长参数： *args
#实际参数的数量大于形式参数的数量的个数,使用*args当做参数以元祖方式把实际参数保存起来
#注意：*args 必须放在形参的最后
'''
#形参：a ，b , *args  实参：11,22,33,44  11给a ,22给b 33和44以元祖的方式保存在*args中
def test1(a,b,*args):
    """求实际参数传入的值的和"""
    #print(a)
    #print(b)
    #print(args)
    sum = a + b
    for temp in args:
        sum += temp
    return  sum
result = test1(11,22,33,44)
print(result)
'''

#（4）不定长参数：**kwargs
#多余的实参如果没有变量名传递给形参args以元祖的方式保存
#多余的实参如果有变量名=value传递给形参**args以字典的方式保存
'''
def test1(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
test1(11,22,33,44,55,66,task=100,done=90)   #这里11,22分别给形参a和b,33,44,55,66以元祖的方式保存在args形参中,task=100,done=90以字典的方式保存在形参kwargs中
'''

#（5）拆包：元祖和列表当做参数
'''
def test1(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
A = (44,55,66)
B = {"name":"tom"}
test1(11,22,A,B)    #默认情况下会把多余的参数作为元祖的元素传入到args参数中形成元祖
test1(11,22,*A,**B) #把A和B分别传入到args和kwargs参数前面需要加*,
'''


