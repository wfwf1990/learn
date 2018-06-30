# Author: wangfang
a = [100]
def test(num):          #列表是可变类型，如果函数想修改该变量，不需要global声明
    #num += num        #如果num是可变类型，+= 直接修改变量
    num = num + num     #如果num是可变类型 重新开辟一个内存空间保存num + num的值
    print(num)
test(a)
print(a)
