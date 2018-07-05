class Person(object):
    def __init__(self,name):
        self.name = name
        self.qiang = None           #用来保存枪的引用
        self.hp = 100
    def __str__(self):
        if self.qiang:
            return "%s的血量是%d，他有枪" %(self.name,self.hp)
        else:
            if self.hp >0:
                return "%s的血量是%d, 没有枪" %(self.name,self.hp)
            else:
                return "%s挂了" %self.name
    #安装子弹到弹夹中
    def anzhuang_zidan_danjia(self,danjia_temp,zidan_temp):
        #弹夹保存子弹，所以需要在弹夹类中创建方法用于保存子弹
        danjia_temp.save_zidan(zidan_temp)
    #老王把弹夹安装到枪中
    def anzhuang_danjia_gun(self,danjia_temp,gun_temp):
        #枪.安装弹夹(弹夹)
        gun_temp.anzhuangdanjia(danjia_temp)

    #老王拿枪
    def na_qiang(self, gun_temp):
        self.qiang = gun_temp       #接收枪对象的引用

    #老王开枪
    def kai_qiang(self,per_temp):
        self.qiang.fire(per_temp)       #枪开火射击子弹

    def diao_xue(self,shanghai_temp):
        self.hp -= shanghai_temp


class Gun(object):
    def __init__(self,name):
        self.name = name
        self.danjia = None

    def __str__(self):
        if self.danjia:
            return "枪是 %s 弹夹信息%s " %(self.name,self.danjia )
        else:
            return "枪是 %s 没有弹夹.." %(self.name)

    def anzhuangdanjia(self,danjia):
        self.danjia = danjia

    def fire(self,per_temp):
        """枪从弹夹中获取一发子弹，然后让这发子弹击中敌人"""
        #先从弹夹中取出子弹
        zidan = self.danjia.qu_chu_zidan()
        #print(zidan)
        if zidan:
            #子弹.打中敌人
            # 让这个子弹去伤害敌人
            zidan.shang_hai_diren(per_temp)
        else:
            print("没有子弹了")





class DanJia(object):
    def __init__(self,num):
        self.num = num          #弹夹的最大容量
        self.zidan = []         #创建一个列表保存子弹

    def __str__(self):
        return "弹夹的容量%d/%d" %(len(self.zidan),self.num)
    def save_zidan(self,zidan):
        self.zidan.append(zidan)

    def qu_chu_zidan(self):
        """ 取出子弹"""
        if self.zidan:
            return  self.zidan.pop()
        else:
            return None

class ZiDan(object):
    def __init__(self,num):
        self.num = num          #子弹的伤害

    def shang_hai_diren(self,per_temp):
        """让人掉血"""
        #人.掉血(子弹的伤害)
        per_temp.diao_xue(self.num)

def main():
    #1丶创建老王对象
    laowang = Person("laowang")
    #2丶创建一个枪对象
    ak47 = Gun("ak47")
    #3丶创建一个弹夹对象
    danjia = DanJia(20)
    for i in range(15):
    #4丶创建一些子弹对象
        zidan = ZiDan(10)
    #5丶老王把子弹安装到弹夹中
        laowang.anzhuang_zidan_danjia(danjia,zidan)
    #6丶老王把弹夹安装到枪中
    laowang.anzhuang_danjia_gun(danjia,ak47)

    #测试弹夹的信息
    #print(danjia)
    #测试枪的信息
    #print(ak47)
    #7丶老王拿枪
    laowang.na_qiang(ak47)
    print(laowang)
    #8丶创建一个敌人
    laosong = Person("隔壁老宋")
    print(laosong)
    #9丶老王开枪打敌人
    laowang.kai_qiang(laosong)
    print(laosong)
    laowang.kai_qiang(laosong)
    print(laosong)
    laowang.kai_qiang(laosong)
    print(laosong)
    laowang.kai_qiang(laosong)
    print(laosong)
    laowang.kai_qiang(laosong)
    print(laosong)
    laowang.kai_qiang(laosong)
    print(laosong)
    laowang.kai_qiang(laosong)
    print(laosong)
    laowang.kai_qiang(laosong)
    print(laosong)
    laowang.kai_qiang(laosong)
    print(laosong)
    laowang.kai_qiang(laosong)
    print(laosong)
    laowang.kai_qiang(laosong)
    print(laosong)
    laowang.kai_qiang(laosong)
if __name__ == "__main__":
    main()