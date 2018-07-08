# Author: wangfang

#threading.enumerate() 查看当前运行的线程数量（包括主线程和子线程）
import time
import threading

def sing():
    """唱歌5秒钟"""
    for i in range(5):
        print("---唱歌中---")
        time.sleep(1)

def dance():
    for i in range(5):
        print("---跳舞中---")
        time.sleep(1)

def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()
    while True:
        print(threading.enumerate())
        if len(threading.enumerate()) <=1:      #子线程执行完毕，只剩下主线程结束循环
            break
        time.sleep(1)
if __name__ == "__main__":
    main()