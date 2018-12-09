import pygame,sys

screen=pygame.display.set_mode((1280,800))
pygame.display.set_caption('training')
bg_color=(0,0,255)
image1=pygame.image.load('images/girl.bmp')
rect=image1.get_rect()
rect.center=screen.get_rect().center
while True:
    for event in pygame.event.get():
        if event==pygame.QUIT:
            sys.exit()
    screen.fill(bg_color)
    screen.get_rect().center
    screen.blit(image1,rect)

    pygame.display.flip()#千万不能忘记啊
run_game()
