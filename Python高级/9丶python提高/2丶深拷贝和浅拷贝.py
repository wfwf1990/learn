# Author: wangfang
#（1）浅拷贝：浅拷贝是对于一个对象的顶层拷贝，通俗的理解是：拷贝了引用，并没有拷贝内容
import copy
"""
a = [11,22]
b = [33,44]
c = [a,b]
print(id(c))
d = copy.copy(c)
print(id(d))
print(id(c[0]))
print(id(d[0]))
#浅拷贝只会拷贝最上面的列表
"""
"""
a = 1            #a指向变量的引用
b = copy.copy(a)
print(id(a))
print(id(b))

c = [11,22]
d = c
print(id(c))
print(id(d))

c = [11,22]
d = copy.copy(c)
print(id(c))
print(id(d))
"""
#总结：
"""
浅拷贝对不可变类型和可变类型的copy不同
copy.copy对于可变类型，会进行浅拷贝
copy.copy对于不可变类型，不会拷贝，仅仅是指向
"""

#（2）深拷贝:深拷贝是对于一个对象所有层次的拷贝(递归)
#深拷贝对列表中的所有的数据引用进行拷贝，而不是只copy a指向列表的引用
"""
a = [11,22]
b = copy.deepcopy(a)
print(a)
print(b)
print(id(a))
print(id(b))
a.append(33)
print(a)
print(b)
"""
"""
a = [11,22]
b = [33,44]
c = [a,b]
d = copy.deepcopy(c)
print(c)
print(d)
print(id(c))
print(id(d))
print(id(c[0]))
print(id(d[0]))
"""

#（3）
a = [11,22]
b = [33,44]
c = [a,b]
d = c[:]
print(c)
print(d)
print(id(c))
print(id(d))
print(id(c[0]))
print(id(d[0]))
#d = c[:] 和d = copy.copy(c) 一样，都是浅拷贝，