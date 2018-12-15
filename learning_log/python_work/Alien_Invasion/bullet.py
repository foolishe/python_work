import pygame
from pygame.sprite import Sprite
import time

class Bullet(Sprite):
    def __init__(self,aliens_settings,screen,ship):
        super(Bullet,self).__init__()
        self.screen=screen
        self.rect=pygame.Rect(0,0,aliens_settings.bullet_width,aliens_settings.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top
        self.y=float(self.rect.y)
        self.color=aliens_settings.bullet_color
        self.speed=aliens_settings.bullet_speed_factor
    def update(self):
        self.y-=self.speed
        self.rect.y=self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
