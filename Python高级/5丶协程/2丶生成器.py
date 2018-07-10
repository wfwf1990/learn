# Author: wangfang
#（1）生成器generator：是一类特殊的迭代器
#（2）创建生成器
#1丶方式1：只要把一个列表生成式的 [ ] 改成 ( )
'''
list1 = [ x*2 for x in range(5)]
print(list1)
G = ( x*2 for x in range(5))
print(G)
print(next(G))      #可以使用next()函数打印生成器里面的值
for item in G:      #使用for循环
    print(item)
'''
#2丶方式2：函数中如果有yield就是一个生成器
'''
def feibo(num):
    a = 0
    b = 1
    count = 0
    while count < num:
        yield a
        a,b = b,a+b
        count += 1

#如果在调用feibo的时候，发现这个函数中有yield那么此时，不是调用函数，而是创建一个生成器对象
ret = feibo(10)
print(ret)
print(next(ret))
for item in ret:
    print(item)
'''
#（3）捕获生成器的返回值，通过异常处理value返回
'''
def feibo(num):
    a = 0
    b = 1
    count = 0
    while count < num:
        yield a
        a,b = b,a+b
        count += 1
    return "done"
#如果在调用feibo的时候，发现这个函数中有yield那么此时，不是调用函数，而是创建一个生成器对象
ret1 = feibo(10)
while True:
    try:
        value = next(ret1)
        print("value:%d" %value)
    except StopIteration as ret:
        print("返回值%s" %ret.value)
        break 
'''
#（4）总结
'''
使用了yield关键字的函数不再是函数，而是生成器。（使用了yield的函数就是生成器）
yield关键字有两点作用：
保存当前运行状态（断点），然后暂停执行，即将生成器（函数）挂起
将yield关键字后面表达式的值作为返回值返回，此时可以理解为起到了return的作用
可以使用next()函数让生成器从断点处继续执行，即唤醒生成器（函数）
Python3中的生成器可以使用return返回最终运行的返回值，而Python2中的生成器不允许使用return返回一个返回值（即可以使用return从生成器中退出，但return后不能有任何表达式）。
'''
#（5）send唤醒：可以使用next()函数唤醒生成器继续执行,还可以使用send()函数唤醒执行,同时还可以向断点处传入一个附加数据

def gen():
    i = 0
    while i < 5:
        ret = yield i
        print(ret)
        i += 1

f = gen()
print(next(f))
f.send("haha")
print(next(f))