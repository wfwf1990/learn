




#人开枪射击子弹

#创建人对象

#创建枪对象

#创建子弹对象

#人把子弹装进枪

#人获取枪

#人开枪射击子弹


class Person(object):
    def __init__(self,name):
        self.name = name
        self.gun = None
    #人把子弹装进枪
    def input_bullet_gun(self,gum_temp,bullet_temp):
        #枪装子弹
        gum_temp.input_bullet(bullet_temp)

    def get_gun(self,gun_temp):
        self.gun = gun_temp

    def __str__(self):
        return  "%s的%s" %(self.name,self.gun)

    def shoot(self):
        #枪射击子弹
        self.gun.fire()

class Gun(object):
    def __init__(self,name):
        self.name = name
        self.bullet_num = 0

        #枪装子弹
    def input_bullet(self,bullet_temp):
        self.bullet_num = bullet_temp.num

    def __str__(self):
        return "%s的子弹数量是%d" %(self.name,self.bullet_num)

    def fire(self):
        if self.bullet_num >0:
            self.bullet_num -= 1
            print("射击一发子弹...，剩余子弹为%d" %self.bullet_num)
        else:
            print("子弹不够了..")


class Bullet(object):
    def __init__(self,num):
        self.num = num
    def __str__(self):
        return "子弹数量%d" %self.num

laowang = Person("laowang")
m4 = Gun("m4")
bullet = Bullet(5)

#laowang.子弹装进枪(m4,bullet)
laowang.input_bullet_gun(m4,bullet)


#laowang获取枪
laowang.get_gun(m4)

#print(bullet)
#print(m4)
print(laowang)

#laowang开枪
laowang.shoot()
laowang.shoot()
laowang.shoot()
laowang.shoot()
laowang.shoot()
laowang.shoot()