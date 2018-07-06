#coding=utf-8
import pygame
from pygame.locals import *
import time

def main():
    #1丶创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480,852))

    #2丶创建一个和窗口大小的图片，用来充当图片
    background = pygame.image.load(r"C:\Users\admin.龙港的阿飞-PC\PycharmProjects\learn\Python基础\12丶飞机大战\feiji\background.png")

    #3丶把背景图片放在窗口显示
    while True:

        #设定需要显示的背景图，窗口对象中加入背景图
        screen.blit(background,(0,0))

        #更新显示的内容
        pygame.display.update()
        time.sleep(1)
if __name__ == "__main__":
    main()