# Author: wangfang


import time
import threading

def sing():
    """唱歌5秒钟"""
    for i in range(5):
        print("---唱歌中---")

def main():
    #在创建线程对象之前打印线程数量
    print(threading.enumerate())

    t1 = threading.Thread(target=sing)
    #在创建线程对象之后打印线程数量
    print(threading.enumerate())


    t1.start()
    #在调用start方法之后打印线程数量
    print(threading.enumerate())

if __name__ == "__main__":
    main()

#总结：创建子线程是在调用start方法之后创建的