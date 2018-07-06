# coding=utf-8
import pygame
from pygame.locals import *
import time


def main():
    # 1丶创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480, 852))

    # 2丶创建一个和窗口大小的图片，用来充当图片
    background = pygame.image.load(
        r"C:\Users\admin.龙港的阿飞-PC\PycharmProjects\learn\Python基础\12丶飞机大战\feiji\background.png")

    #3丶创建一个飞机图片
    feiji = pygame.image.load(r"C:\Users\admin.龙港的阿飞-PC\PycharmProjects\learn\Python基础\12丶飞机大战\feiji\hero1.png")

    x = 190
    y = 700

    # 3丶把背景图片放在窗口显示
    while True:
        # 设定需要显示的背景图，窗口对象中加入背景图
        screen.blit(background, (0, 0))

        #飞机图加入到窗口
        screen.blit(feiji,(x,y))

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
                    x -= 10
                # 检测按键是否是d或者right
                elif event.key == K_d or event.key == K_RIGHT:
                    print('right')
                    x += 10

                # 检测按键是否是空格键
                elif event.key == K_SPACE:
                    print('space')

        # 更新显示的内容
        pygame.display.update()



if __name__ == "__main__":
    main()