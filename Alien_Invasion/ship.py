import pygame
from bullet import Bullet
import time
from pygame.sprite import Sprite

class Ship(Sprite):
    bullet_time=0.1
    def __init__(self,screen,aliens_settings):
        super(Ship,self).__init__()
        self.screen=screen
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()#获取图像的矩形模型
        self.screen_rect=screen.get_rect()
        self.rect.centerx=self.screen_rect.centerx#self.image.get_rect().centerx=screen.get_rect().centerx
        self.rect.bottom=self.screen_rect.bottom
        self.aliens_settings=aliens_settings
        self.moving_left=False
        self.moving_right=False
        self.centerx=self.rect.centerx
        self.fire=False

    def fire_bullet(self,ship,bullets):
        if self.fire and len(bullets) < self.aliens_settings.bullets_allowed and \
        time.perf_counter()-self.bullet_time>0.2:
            new_bullet=Bullet(self.aliens_settings,self.screen,ship)
            bullets.add(new_bullet)
            self.bullet_time=time.perf_counter()
    def update(self):
        if self.moving_left and 0<self.rect.centerx:
            self.centerx-=self.aliens_settings.ship_speed_factor
        if self.moving_right and self.screen_rect.right>self.rect.centerx:
            self.centerx+=self.aliens_settings.ship_speed_factor
        self.rect.centerx=self.centerx
    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.center=self.screen_rect.centerx
