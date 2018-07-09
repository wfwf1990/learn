
path1 = r'C:\Users\admin.龙港的阿飞-PC\Desktop\1\sql\20170709'
path2 = r'C:\Users\admin.龙港的阿飞-PC\Desktop\1\sql\20170709'
import time
import os
new_file_list = []
fileList = os.listdir(path1)
for temp in fileList:
    if temp.endswith(".sql"):
        new_file_list.append(temp)
print(new_file_list)

for temp in new_file_list:
    #print(i)
    #file1 = os.path.join(path1,temp +".sql")
    #file2 = os.path.join(path2,"new_" + temp +".sql")
    file1 = file1 = os.path.join(path1,temp)
    file2 = os.path.join(path2, "new_" + temp)
    print(file1)
    print(file2)
    with open(file1, "r", encoding="utf-8") as f1:
        while True:
            try:
                t1 = f1.readline()
                i1 = "`" + temp + "`"
                # time.sleep(0.01)
                #print(t1)
                if len(t1) < 5:
                    break
                with open(file2, "a", encoding="utf-8") as f2:
                    f2.write(t1.replace("``", i1))
                    f2.write("\n")
            except:
                break
'''
with open(path,"r",encoding="utf-8") as f1:
    while True:
        try:
            t1 = f1.readline().strip()
            #time.sleep(0.01)
            print(t1)
            if len(t1) < 5:
                break
            with open(path1,"a",encoding="utf-8") as f2:
                f2.write(t1.replace("``","`tbl_user_bill`"))
                f2.write("\n")
        except:
            break
'''