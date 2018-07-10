import time
import multiprocessing
import os

def test1():
    """子进程要执行的代码"""
    while True:
        print("子进程test1运行中,pid=%d,父进程的pid=%d" %(os.getpid(),os.getppid()))
        print("--------1---------")
        time.sleep(1)

def test2():
    """子进程要执行的代码"""
    while True:
        print("子进程test2运行中,pid=%d,父进程的pid=%d" %(os.getpid(),os.getppid()))
        print("--------2---------")
        time.sleep(1)

def main():
    print("主进程运行中,pid=%d,父进程的pid=%d" % (os.getpid(), os.getppid()))
    p1 = multiprocessing.Process(target=test1)      #通过multiprocessing中的Process类创建对象，创建子进程只需要传入一个执行函数和函数的参数
    p2 = multiprocessing.Process(target=test2)

    p1.start()      #使用start()方法启动
    p2.start()
    p1.join(10)       #等待子进程执行结束,主进程才会结束,超时时间10秒
    p2.join(10)

if __name__ == "__main__":
    main()