
'''
with open(path,"r",encoding="utf-8") as f1:
    while True:
        try:
            t1 = f1.readline().strip()
            #time.sleep(0.01)
            print(t1)
            with open(path1,"a",encoding="utf-8") as f2:
                f2.write(t1.replace("``","`tbl_user_bill`"))
                f2.write("\n")
        except:
            break

'''
'''
with open(path,"r",encoding="utf-8") as f1:
    while True:
            t1 = f1.readline().strip()
            #time.sleep(0.01)
            print(t1)
            if len(t1) < 5:
                break

'''
path = r'C:\Users\admin.龙港的阿飞-PC\Desktop\1\sql\20180628\tbl_mail_order.sql'
path1 = r'C:\Users\admin.龙港的阿飞-PC\Desktop\1\sql\20180628\tbl_mail_order1.sql'
import time
with open(path,"r",encoding="utf-8") as f1:
    while True:
        try:
            t1 = f1.readline().strip()
            #time.sleep(0.01)
            print(t1)
            if len(t1) < 5:
                break
            with open(path1,"a",encoding="utf-8") as f2:
                f2.write(t1.replace("``","`tbl_mail_order`"))
                f2.write("\n")
        except:
            break