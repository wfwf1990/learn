# Author: wangfang
#定义子弹类：子弹数量
class Bullet:
    def __init__(self,new_bullet_num):
        self.bullet_num = new_bullet_num
        self.left_bullet_number = new_bullet_num
    def __str__(self):
        msg = "枪的子弹总计为%d发,剩余子弹为%d发" %(self.bullet_num,self.left_bullet_number)
        return  msg

class Gun:
    def __init__(self,bullet):
        self.bullet_num = bullet.bullet_num
        self.left_bullet_num = bullet.bullet_num
        self.shoot_num = 0

    def Shooting(self):     #射击
        if self.left_bullet_num  >  0:
            self.left_bullet_num -= 1
            self.shoot_num += 1
            print("开了%d枪，还剩余%d发子弹" %(self.shoot_num,self.left_bullet_num))
        else:
            print("子弹不够了")
    def AddGunBullet(self,num):
        self.left_bullet_num += num


class Person:
    def __init__(self):
        pass
    def ShootGun(self,gun):
        gun.Shooting()


bullet = Bullet(2)
print(bullet)
gun = Gun(bullet)
per = Person()
per.ShootGun(gun)
per.ShootGun(gun)
per.ShootGun(gun)
gun.AddGunBullet(2)
per.ShootGun(gun)
per.ShootGun(gun)
per.ShootGun(gun)
gun.AddGunBullet(2)
per.ShootGun(gun)