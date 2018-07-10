# Author: wangfang
#（1）协程：实现多任务的一种方式，多任务的执行只是单纯的cpu的上下文切换,也还只是在一个线程里面

#（2）线程的实现：yield
import time
def test1():
    while True:
        print("work1")
        yield
        time.sleep(0.5)
def test2():
    while True:
        print("work2")
        yield
        time.sleep(0.5)

def main():
    t1 = test1()        #创建一个生成器
    t2 = test2()
    #先让t1运行，让遇到yield的时候，在返回23行,
    #执行t2，当它遇到yield的时候，再次切换t1
    #这样t1和t2交替运行，最终实现多协程
    while True:
        next(t1)
        next(t2)

if __name__ == "__main__":
    main()