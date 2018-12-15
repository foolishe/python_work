import random

class Settings():
    #设置类
    def __init__(self):
        self.screen_width=1200#窗口设置
        self.screen_height=800
        self.bg_color=(230,230,230)
        #self.ship_speed_factor=1.5 #ship setting
        self.ship_limit=3
        #self.bullet_speed_factor=1# 子弹设置
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=60,60,60
        self.bullets_allowed=10
        #self.alien_speed=1
        self.fleet_drop_speed=10
        self.fleet_direction=1
        self.alien_point=50

    def speed_factor(self):
        self.alien_speed=1.3
        self.bullet_speed_factor=1.5
        self.ship_speed_factor=1.5
        self.alien_point=50

    def speed_increase(self):
         self.alien_speed+=0.5
         self.bullet_speed_factor+=1
         self.ship_speed_factor+=1
         self.alien_point+=random.choice([20,30,40,50])
