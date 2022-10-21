import sys
import pygame

#http://c.biancheng.net/pygame/display.html



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
        #refresh all screen
        pygame.display.flip()

        #可以根据选定的区域来更新部分内容，如果没有提供区域位置参数时，其作用和 display.flip() 相同
        # pygame.display.update() 






if __name__ == '__main__':    
    main()