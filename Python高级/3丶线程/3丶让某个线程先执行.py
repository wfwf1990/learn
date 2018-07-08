# Author: wangfang

import time
import threading

def sing():
    """唱歌5秒钟"""
    for i in range(5):
        print("---唱歌中---")


def dance():
    for i in range(5):
        print("---跳舞中---")


def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    time.sleep(1)
    t2.start()

if __name__ == "__main__":
    main()