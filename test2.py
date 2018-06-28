
path1 = r'C:\Users\admin.龙港的阿飞-PC\Desktop\1\sql\20180628'
path2 = r'C:\Users\admin.龙港的阿飞-PC\Desktop\1\sql\sql'
import time
import os
fileList = ["tbl_user_bill","tbl_user_bill_business_relation","tbl_mail_order"]
for i in fileList:
    #print(i)
    file1 = os.path.join(path1,i +".sql")
    file2 = os.path.join(path2,i +".sql")
    print(file1)
    print(file2)
    with open(file1, "r", encoding="utf-8") as f1:
        while True:
            try:
                t1 = f1.readline().strip()
                i1 = "`" + i + "`"
                # time.sleep(0.01)
                print(t1)
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