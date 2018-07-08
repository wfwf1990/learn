# Author: wangfang
import threading
import time

num = 0
def test1():
    global num
    for i in range(1000000):
        num += 1
    print("----- in test1 num = %d" %num)
def test2():
    global num
    for i in range(1000000):
        num += 1
    print("----- in test2 num = %d" % num)

def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)
    t1.start()
    t2.start()

    #等待子线程执行结束
    time.sleep(5)
    print("----- in main num = %d" % num)


if __name__ == "__main__":
    main()

#总结：如果多个线程同时对同一个全局变量操作，会出现资源竞争问题，从而数据结果会不正确