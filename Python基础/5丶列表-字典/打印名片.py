# Author: wangfang

#打印菜单
print("#"*20)
print("1丶添加一个名片".center(15))
print("2丶删除一个名片".center(15))
print("3丶修改一个名片".center(15))
print("4丶查询一个名片".center(15))
print("5丶打印所有名片".center(15))
print("6丶退出".center(15))
print("#"*20)

#定义列表保存用户的信息
new_infos = [{"name":"123","age":"123","qq":"123","phone":"123"}]

while True:
    #等待用户输入
    num = input("请输入一个数字:")

    #判断用户输入的是否是数字，如果是字符串重新输入
    if not num.isdigit():
        print("请输入数字...")
        continue
    input_num = int(num)

    #判断用户输入
    if input_num == 1:      #添加用户信息
        new_name = input("请输入姓名:")
        new_qq = input("请输入qq:")
        new_phone = input("请输入手机号码:")
        new_age = input("请输入你的年龄:")

        #定义空字典，用户输入的信息存入到字典中
        user_info = {}
        user_info["name"] = new_name
        user_info["qq"] = new_qq
        user_info["phone"] = new_phone
        user_info["age"] = new_age
        #new_infos.append(user_info)

        #循环列表，判断列表中的字典的key值是否和用户输入的值相同，相同表示用户存在
        for temp in new_infos:
            if temp.get("name") == user_info["name"]:
                print("用户信息已存在....")
                break
        new_infos.append(user_info)

    elif input_num == 2:
        # 等待用户输入
        find_name = input("请输入你要删除的姓名:")

        # 判断用户是否存在，如果用户存在，通过获取列表的下标进行对列表下标的元素进行删除
        # 定义一个临时变量，通过对临时变量进行判断用户是否存在

        find_flag = 0
        for temp in new_infos:
            if temp['name'] == find_name:
                #print("%s\t%s\t%s\t%s" % (temp['name'], temp['age'], temp['qq'], temp['phone']))
                del_index = new_infos.index(temp)
                del new_infos[del_index]
                find_flag += 1
                break
        if find_flag == 0:
            print("查无此人...")
    elif input_num == 3:
        #等待用户输入
        find_name = input("请输入你要修改的姓名:")

        #判断用户是否存在，如果用户存在，通过获取字典的key值等于新值
        #定义一个临时变量，通过对临时变量进行判断用户是否存在
        find_flag = 0
        for temp in new_infos:
            if temp['name'] == find_name:
                #print("%s\t%s\t%s\t%s" %(temp['name'],temp['age'],temp['qq'],temp['phone']))
                new_name = input("请输入姓名:")
                new_qq = input("请输入qq:")
                new_phone = input("请输入手机号码:")
                new_age = input("请输入你的年龄:")
                user_info["name"] = new_name
                user_info["qq"] = new_qq
                user_info["phone"] = new_phone
                user_info["age"] = new_age
                temp['name'] = new_name
                temp['qq'] = new_qq
                temp['phone'] = new_phone
                temp['age'] = new_age
                find_flag += 1
                break
    elif input_num == 4:

        #等待用户输入
        find_name = input("请输入你要查找的姓名:")

        #判断用户是否存在
        #定义一个临时变量，通过对临时变量进行判断用户是否存在
        find_flag = 0
        for temp in new_infos:
            if temp['name'] == find_name:
                print("%s\t%s\t%s\t%s" %(temp['name'],temp['age'],temp['qq'],temp['phone']))
                find_flag += 1
                break
        if find_flag == 0:
            print("查无此人...")
    elif input_num == 5:
        print("姓名\tqq\tphone\tage")
        for temp in new_infos:
            print("%s\t%s\t%s\t%s" % (temp['name'], temp['age'], temp['qq'], temp['phone']))
    elif input_num == 6:
        break
    else:
        print("请输入正确的数字....")

