# Author: wangfang
import threading
import time

num1 = [10,20]

def test1(temp):
    temp.append(30)
    print("------in test1 num=%s" %str(temp))

def test2(temp):
    print("-----in test2 num=%s" %str(temp))


def main():
    t1 = threading.Thread(target=test1,args=(num1,))
    t2 = threading.Thread(target=test2,args=(num1,))

    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)
    print("----in main num = %s" %str(num1))

if __name__ == "__main__":
    main()

#把全局变量作为实际参数，传入到子线程调用的函数作为形参，需要使用args=元祖



