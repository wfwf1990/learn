
import time
import multiprocessing

def test1():
    """子进程要执行的代码"""
    while True:
        print("--------1---------")
        time.sleep(1)

def test2():
    """子进程要执行的代码"""
    while True:
        print("--------2---------")
        time.sleep(1)

def main():
    p1 = multiprocessing.Process(target=test1)      #通过multiprocessing中的Process类创建对象，创建子进程只需要传入一个执行函数和函数的参数
    p2 = multiprocessing.Process(target=test2)

    p1.start()      #使用start()方法启动
    p2.start()



if __name__ == "__main__":
    main()