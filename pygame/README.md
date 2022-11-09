# pygame
參考網址：http://c.biancheng.net/pygame/surface.html

#等待事件发生

    # event = pygame.event.wait()
    # if event.type == pygame.QUIT:
    #     exit()
    # if event.type == pygame.MOUSEBUTTONDOWN:
    #     print('鼠标按下',event.pos)
    # if event.type == pygame.MOUSEBUTTONUP:
    #     print('鼠标弹起')
    # if event.type == pygame.MOUSEMOTION:
    #     print('鼠标移动')
    #     # 键盘事件
    # if event.type ==pygame.KEYDOWN:
    #     # 打印按键的英文字符
    #     print('键盘按下',chr(event.key))
    # if event.type == pygame.KEYUP:
    #     print('键盘弹起')

    site = [0, 0]
    # 移动图像
    position = position.move(site)