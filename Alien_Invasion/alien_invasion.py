import sys,pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    pygame.init()
    aliens_settings=Settings()
    screen=pygame.display.set_mode((aliens_settings.screen_width,aliens_settings.screen_height))
    pygame.display.set_caption('Alien Incasion')
    ship=Ship(screen,aliens_settings)
    bullets=Group()
    while True: #每次循环都会自动重绘屏幕
        gf.check_events(aliens_settings,screen,ship,bullets)
        gf.update_screen(aliens_settings,screen,ship,bullets)#更新屏幕上的图像,并切换到新屏幕
run_game()
