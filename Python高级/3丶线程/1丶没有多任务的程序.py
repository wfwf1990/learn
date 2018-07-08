# Author: wangfang

import time
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
    sing()
    dance()

if __name__ == "__main__":
    main()