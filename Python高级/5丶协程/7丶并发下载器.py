# Author: wangfang

from gevent import monkey
import gevent
import random
import time
import urllib.request

# 有耗时操作时需要
monkey.patch_all()  # 将程序中用到的耗时操作的代码，换为gevent中自己实现的模块
def download_jpg(file,temp):
    ret = urllib.request.urlopen(temp)
    data = ret.read()
    with open(file,"wb")as f1:
        f1.write(data)


gevent.joinall([
        gevent.spawn(download_jpg,"1.jpg","http://ui.sina.com/assets/img/www/worldmap.jpg"),
        gevent.spawn(download_jpg, "2.jpg","http://n.sinaimg.cn/news/175/w105h70/20180710/7OVY-hezpzwu5038087.gif")
])