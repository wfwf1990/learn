# Author: wangfang
import threading
import time

num1 = 100

def test1():
    global  num1
    num1 += 100
    print("------in test1 num=%d" %num1)

def test2():
    print("-----in test2 num=%d" %num1)


def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)

    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)
    print("----in main num = %d" %num1)

if __name__ == "__main__":
    main()

#总结：在一个进程内的所有线程全局变量是共享的，方便多个线程之间的调用
#缺点就是，线程是对全局变量随意遂改可能造成多线程之间对全局变量的混乱（即线程非安全）

