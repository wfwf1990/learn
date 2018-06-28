myStr = "hello world itcast and itcastxxxcpp"


print(myStr.find("1"))      #从左边开始查找元素在字符串中的起始下标，如果查找到，返回第一个查询的元素的下标位置,如果没有查找到返回-1
print(myStr.rfind("itcast"))    #从右边开始查找元素在字符串中的起始下标

print(myStr.index("w"))  #同find功能相似,从左边开始查找,如果查找到返回元组在字符串中的下标位置，如果没查找到,报异常
print(myStr.rindex("w")) #同find功能相似,从右边开始查找,如果查找到返回元组在字符串中的下标位置，如果没查找到,报异常

print(myStr.count("itcast")) #统计元素在字符串中的个数

print(myStr.replace("itcast","nice"))       #把str1替换成str2
print(myStr.replace("itcast","nice",1))     #替换1次

print(myStr.split(" "))     #切割