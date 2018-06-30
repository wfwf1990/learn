# Author: wangfang

#（1）匿名函数应用：列表排序
#列表排序
list1 = [11,2,3,123,12312]
list1.sort()        #升序
list1.sort(reverse=True)        #降序

#（2）列表中如果有字典排序
list2 = [{"name":"laowang","age":18},{"name":"xiaowang","age":33},{"name":"zhangtao","age":20}]
list2.sort(key= lambda x:x["name"]) #使用lambda获取列表中的字典的key值排序,这里根据key是name排序
print(list2)
list2.sort(key= lambda  x:x["age"]) #根据key是age排序
print(list2)

#（3）匿名函数作为参数传递 :计算两个数的和
#lambda表达式当做实参传到函数,函数接收该参数执行该函数，其中lambda表达式需要两个变量,所以函数执行该函数必须传递两个值
#lambda表达式执行完之后会返回表达式执行的结果，使用result变量接收该结果，使用return返回该变量
def fun(a,b,func):
    result = func(a,b)
    return result
res = fun(11,22,lambda x,y:x+y)
print(res)

#（4）input输入匿名函数当做参数传递函数
def test1(a,b,func):
    result = func(a,b)
    return  result

exp = input("请输入一个lambda表达式：")
exp = eval(exp)     #python3 input输入表达式也会把表达式当做字符串处理，所以这里需要通过eval函数把字符串中的表达式处理成表达式
res = test1(11,22,exp)
print(res)