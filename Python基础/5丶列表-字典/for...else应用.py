

#for...else语句
#for循环遍历完列表中的元素，才会执行else语句；
#如果不想执行else语句，可以在for循环遍历列表的时候加break
nums = [11,22,33]
for num in nums:
    print(num)
else:
    print("="*10)


#应用：查询列表中的用户是否存在，如果用户存在打印用户存在，否则提示用户不存在

#定义列表
card_infos = [{"name":"laowang","age":"18"},{"name":"laoli","age":"20"}]

#等待用户输入
find_name = input("请输入你要查询的用户名:")
#遍历列表，列表中的元素是字典，根据key取字典的values值 和用户输入的用户名进行比较是否相同，如果存在break结束循环,反之执行else语句
for temp in card_infos:
    if temp["name"] == find_name:
        print("用户存在...")
        break
else:
    print("用户不存在...")
