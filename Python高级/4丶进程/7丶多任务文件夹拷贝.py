import os
import multiprocessing

def copy_2_file(file_name,new_path,old_path):

    old_abs_file = os.path.join(old_path+"\\" +file_name)
    new_abs_file = os.path.join(new_path+"\\" +file_name)
    #print(old_abs_file)
    #print(new_abs_file)
    with open(old_abs_file, "rb") as f1:
        while True:
            content = f1.read(5)
            with open(new_abs_file,"ab") as f2:
                f2.write(content)
                if len(content) <1:
                    break


def main():
    #指定要复制的目录
    old_path = r"C:\Users\admin.龙港的阿飞-PC\Desktop\1\sql\20180627"

    #创建新的目录
    #path =  "[复制]" + old_path.split("\\")[-1]
    new_path = os.path.join(old_path + "[复制]")
    if not os.path.exists(new_path):
        os.mkdir(new_path)
    else:
        print("目录：%s已存在..." %new_path)
    #获取复制目录下的所有文件
    file_names = os.listdir(old_path)


    #向进程池中添加copy文件任务
    po = multiprocessing.Pool(3)  # 定义一个进程池，最大进程数3
    for file_name in file_names:
        po.apply_async(copy_2_file,(file_name,new_path,old_path))

    po.close()
    po.join()

    #print(old_path)
    #print(new_path)
    #print(file_names)
if __name__ == "__main__":
    main()