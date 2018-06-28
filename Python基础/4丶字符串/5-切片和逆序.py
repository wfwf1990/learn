#切片  ：根据起始下标和终止下标+1
#变量[起始下标:终止下标:步长=1]   步长默认为1
name1 = 'abcdef'
print(name1[2:5])           #只能取2到4的之间的元素
print(name1[2:-1])
print(name1[2:])            #取2到最后一个元素
print(name1[2:-1:2])        #间隔1取元素



#逆序
print(name1[-1::-1])
print(name1[::-1])