
import time
import multiprocessing

num = [11,22]
def test1():
    """子进程要执行的代码"""
    num.append(33)
    print("in test1 num=%s" %str(num))

def test2():
    """子进程要执行的代码"""
    print("in test2 num=%s" % str(num))

def main():
    p1 = multiprocessing.Process(target=test1)      #通过multiprocessing中的Process类创建对象，创建子进程只需要传入一个执行函数和函数的参数
    p2 = multiprocessing.Process(target=test2)

    p1.start()      #使用start()方法启动

    time.sleep(1)       #等待p1子进程结束之后再执行p2子进程
    p2.start()



if __name__ == "__main__":
    main()