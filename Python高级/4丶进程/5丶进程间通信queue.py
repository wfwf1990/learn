#(1)队列：queue 先进先出
'''
import multiprocessing
#创建队列
q = multiprocessing.Queue(3)   #初始化一个Queue对象，最多可接收3条put消息
q.put("消息1")
q.put("消息1")
print(q.full())         #判断队列是否满了，如果满了返回True,反之False
q.get()                 #获取队列中的消息
print(q.empty())        #判断队列是空，如果为空，返回True,反之False

q.put("消息3")
q.put("消息4")
q.put("消息4")
'''

#（2）队列demo 一个进程向queue写数据，一个进程从queue中获取数据
import multiprocessing
def input_data(q):
    """向队列中写数据"""
    #模拟数据
    data = [11,22,33,44,55]
    #向队列中写数据
    for temp in data:
        q.put(temp)
    print("数据已经向队列中写入完毕....")

def output_data(q):
    """向队列中获取数据，进行数据处理"""
    data2 = []
    while True:
        data2.append(q.get())
        if q.empty():
            break
    print("数据已经从队列中读取完毕")
    print(data2)
def main():
   #创建一个队列
    q = multiprocessing.Queue(3)

    #创建进程对象
    p1 = multiprocessing.Process(target=input_data,args=(q,))
    p2 = multiprocessing.Process(target=output_data,args=(q,))

    p1.start()
    p2.start()
if __name__ == "__main__":
    main()