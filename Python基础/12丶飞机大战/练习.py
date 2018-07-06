import pygame
from pygame.locals import *


class Plane(object):
    """飞机类"""
    def __init__(self,screen_temp):
        self.x = 190
        self.y = 700
        self.image = pygame.image.load(r"C:\Users\admin.龙港的阿飞-PC\PycharmProjects\learn\Python基础\12丶飞机大战\feiji\hero1.png")
        self.screen = screen_temp
        self.bullet_list = []       #列表保存子弹
    def display(self):
        """把飞机图加入到窗口中"""
        self.screen.blit(self.image,(self.x,self.y))
        """获取子弹"""
        for bullet in self.bullet_list:
            bullet.display()        #显示子弹
            bullet.move()           #子弹移动

    def move_left(self):
        """飞机向左移动"""
        self.x -= 10
    def move_right(self):
        self.x += 10

    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))        #创建子弹对象，保存到子弹列表中


class EnemyPlane(object):
    """敌机类"""
    def __init__(self,screen_temp):
        self.x = 0
        self.y = 0
        self.image = pygame.image.load(r"C:\Users\admin.龙港的阿飞-PC\PycharmProjects\learn\Python基础\12丶飞机大战\feiji\enemy0.png")
        self.screen = screen_temp
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

    def
class Bullet(object):
    """子弹类"""
    def __init__(self,screen_temp,x,y):
        self.x = x + 40
        self.y = y - 5
        self.screen = screen_temp
        self.image = pygame.image.load(r"C:\Users\admin.龙港的阿飞-PC\PycharmProjects\learn\Python基础\12丶飞机大战\feiji\bullet.png")

    def display(self):
        """把子弹加入到窗口中"""
        self.screen.blit(self.image,(self.x,self.y))

    def move(self):
        self.y -= 10

def input_key(player_plane_temp):
    # 获取事件，比如按键等
    for event in pygame.event.get():

        # 判断是否是点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
        # 判断是否是按下了键
        elif event.type == KEYDOWN:
            # 检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                player_plane_temp.move_left()

            # 检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                player_plane_temp.move_right()
            # 检测按键是否是空格键
            elif event.key == K_SPACE:
                print('space')
                player_plane_temp.fire()

def main():
    # 1. 创建窗口对象
    screen = pygame.display.set_mode((480, 890), 0, 32)

    #创建一个和窗口大小的背景图
    background = pygame.image.load(
        r"C:\Users\admin.龙港的阿飞-PC\PycharmProjects\learn\Python基础\12丶飞机大战\feiji\background.png")

    # 创建飞机对象
    player_plane = Plane(screen)

    #创建敌机对象
    enemy_plane = EnemyPlane(screen)
    # 3.
    while True:
        #把背景图片放到窗口中显示
        screen.blit(background, (0, 0))

        #显示飞机在窗口上
        player_plane.display()

        #显示敌机
        enemy_plane.display()

        #控制飞机移动
        input_key(player_plane)

        pygame.display.update()

if __name__ == "__main__":
    main()