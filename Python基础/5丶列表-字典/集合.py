
#集合定义
set1 = {11,22,33,44,11,22,33}

#集合默认情况下会去重
print(set1)


#列表去重 ，列表转成集合，集合在转换成列表

list1 = [11,22,33,44,11,22]
set2 = set(list1)
print(set2)
list1 = list(set2)
print(list1)