
import os
import time
import multiprocessing

def run_proc(name,age,*args,**kwargs):
    for temp in range(10):
        print("子进程运行中，name=%s,age=%d,子进程pid=%d" %(name,age,os.getpid()))
        print(args)
        print(kwargs)
        time.sleep(1)


def main():
    p1 = multiprocessing.Process(target=run_proc,args=('tom',20,30,40),kwargs={"mm":18})

    p1.start()
    time.sleep(1)
    p1.terminate()          #1秒之后立即结束子进程
    p1.join()

if __name__ == "__main__":
    main()



