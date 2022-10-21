import sys
import pygame
#引入pygame中所有常量，比如 QUIT
from pygame.locals import *

#http://c.biancheng.net/pygame/time.html



def main():
    pygame.init()
    #initialize

    #set main window
    screen = pygame.display.set_mode((400,400))
        #size:()
        #flags:pygame.RESIZABLE
    #Surface 類似 sprite

    #screen.blit(source, dest, area=None, special_flags = 0)
        #dest：主窗口中的一个标识的坐标位置，可以接受一个 (x,y) 元组，或者 (x,y,width,height) 元组，也可以是一个 Rect 对象；


    #set window title
    pygame.display.set_caption('mouse')
    screen.fill('white')

    face = pygame.Surface((50,50),flags=pygame.HWSURFACE)
    #fill color
    face.fill(color='pink')

    #加载一张图片
    # image_surface = pygame.image.load("C:/Users/Administrator/Desktop/c-net.png").convert()
    # image_new = pygame.transform.scale(image_surface,(300,300))
    # 查看新生成的图片的对象类型
    #print(type(image_new))
    # 对新生成的图像进行旋转至45度
    # image_1 =pygame.transform.rotate(image_new,45)
    # 使用rotozoom() 旋转 0 度，将图像缩小0.5倍
    # image_2 = pygame.transform.rotozoom(image_1,0,0.5)


    #game loop
    while True:
        #listening event status
        for event in pygame.event.get():
            #if X
            if event.type == pygame.QUIT:
                #remove all module
                pygame.quit()
                # end process
                sys.exit()
        #add face to screen
        screen.blit(face, (100,100))

        #refresh all screen
        pygame.display.flip()

        #可以根据选定的区域来更新部分内容，如果没有提供区域位置参数时，其作用和 display.flip() 相同
        # pygame.display.update() 






if __name__ == '__main__':    
    main()