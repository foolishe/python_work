import pygame,sys

screen=pygame.display.set_mode((1280,800))
pygame.display.set_caption('training')
bg_color=(0,0,255)
image1=pygame.image.load('images/ship.bmp')
screen.get_rect().centerx
screen.get_rect().centery
while True:
    for event in pygame.event.get():
        if event==pygame.QUIT:
            sys.exit()

    screen.fill(bg_color)
    screen.blit(image1,image1.get_rect())
    pygame.display.flip()#千万不能忘记啊
run_game()
