#return ：调用函数的执行结果的返回值，可以使用变量保存函数执行的返回值，同时可以结束函数
#(1)return：一个函数利用另外一个函数的返回值
'''
def getTemperature():
    set_temperature = 22
    print("现在的温度是%d" %set_temperature)
    return set_temperature

def getFahrenheit(set_temperature ):
    fahrenheit = set_temperature + 3
    print("现在的华氏温度是%d" %fahrenheit)
result = getTemperature()       #函数执行结果就是return的返回值，使用result变量接收这个返回值
getFahrenheit(result)           #把result变量的值当成实际参数传递给函数getFahrenheit的形式参数,使用变量set_temperature结果形式参数

'''

#(2)函数返回多个值
'''
#函数返回多个值：
def values():
    v1 = 1
    v2 = 2
    v3 = 3

    #返回多个变量的值，可以把多个值封装成列表和元组等数据类型返回
    return  v1,v2,v3    #方式一：这样返回的是元组
    #return (v1,v2,v3)  #方式二：
    list1 = [v1,v2,v3]  #方式三
    #return  list1

result = values()
print(result)
'''
#(2)函数返回多个值：元祖方式
'''
def test(a,b):
    shang = a//b
    yushu = a % b
    return  shang,yushu  #返回的是元祖格式
sh,yu = test(10,2)
print(sh,yu)
#结果sh=5 yu=0 
'''
