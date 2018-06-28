''''''


'''continue：结束当前循环，继续下一次循环'''

i = 1
while i <= 5:

    if i == 3:      #当i == 3结束while循环，继续下一次循环
        i += 1
        continue
    print(i)
    i += 1
print("="*10)     #while循环结束,会执行while并行的语句


#运行结果
'''
1
2
4
5
==========
'''