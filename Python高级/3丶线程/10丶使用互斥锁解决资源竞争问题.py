# Author: wangfang

#（1）互斥锁概念
'''
多个线程几乎同时修改某一个共享数据的时候，需要进行同步控制

线程同步能够保证多个线程安全访问竞争资源，最简单的同步机制是引入互斥锁。

互斥锁为资源引入一个状态：锁定/非锁定

某个线程要更改共享数据时，先将其锁定，此时资源的状态为“锁定”，
其他线程不能更改；直到该线程释放资源，将资源的状态变成“非锁定”，
其他的线程才能再次锁定该资源。互斥锁保证了每次只有一个线程进行写入操作，
从而保证了多线程情况下数据的正确性。

'''

#（2）创建锁，上锁和释放锁
'''
# 创建锁
mutex = threading.Lock()

# 锁定
mutex.acquire()

# 释放
mutex.release()
'''

#（3）方式一：使用互斥锁解决资源竞争问题
'''
import threading
import time

num = 0
def test1():
    global num
    #上锁，如果之前没有锁定，那么此时上锁成功
    #如果上锁之前已经被上锁了，那么此时会堵塞在这里，直到这个锁被揭开位置
    mutex.acquire()
    for i in range(1000000):
        num += 1

    #解锁
    mutex.release()
    print("----- in test1 num = %d" %num)
def test2():
    global num

    #上锁
    mutex.acquire()
    for i in range(1000000):
        num += 1
    #解锁
    mutex.release()
    print("----- in test2 num = %d" % num)

#创建一个互斥锁,默认是没有上锁的
mutex = threading.Lock()

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
'''
#总结：这个方案是线程1上锁，循环结束之后释放锁，线程2上锁，循环结束之后释放锁

#（4）方式二：使用互斥锁解决资源竞争问题
'''
import threading
import time

num = 0
def test1():
    global num
    #上锁，如果之前没有锁定，那么此时上锁成功
    #如果上锁之前已经被上锁了，那么此时会堵塞在这里，直到这个锁被揭开位置
    for i in range(1000000):
        mutex.acquire()
        num += 1
        mutex.release()
    #解锁

    print("----- in test1 num = %d" %num)
def test2():
    global num


    for i in range(1000000):
        # 上锁
        mutex.acquire()
        num += 1
        mutex.release()
    #解锁
    print("----- in test2 num = %d" % num)

#创建一个互斥锁,默认是没有上锁的
mutex = threading.Lock()

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
    
#总结：这种方式两个线程之间每次循环进行上锁和释放锁的操作
'''