import sys,pygame

def check_events():
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

def update_screen(aliens_settings,screen,ship):
    screen.fill(aliens_settings.bg_color) #设置背景颜色
    ship.blitme() #绘制飞船
    pygame.display.flip() #让最近绘制的屏幕可见
