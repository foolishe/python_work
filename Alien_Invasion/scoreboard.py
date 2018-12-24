import pygame.font
from ship import Ship
from pygame.sprite import Group


class Scoreboard():
    def __init__(self,aliens_settings,screen,stats,ship):
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.aliens_settings=aliens_settings
        self.stats=stats
        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None,48)
        self.ship=ship
        self.update_score()
    def update_score(self):
            self.perp_level()
            self.perp_score()
            self.perp_ships()
            self.perp_highest_score()
    def perp_score(self):
        score_str='{:,}'.format(int(round(self.stats.score,-1)))
        self.score_image=self.font.render(score_str,True,self.text_color,self.aliens_settings.bg_color)
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right-20
        self.score_rect.top=20

    def perp_highest_score(self):
        score_str='{:,}'.format(int(round(self.stats.highest_score,-1)))
        self.highest_score_image=self.font.render(score_str,True,self.text_color,self.aliens_settings.bg_color)
        self.highest_score_rect=self.highest_score_image.get_rect()
        self.highest_score_rect.centerx=self.screen_rect.centerx
        self.highest_score_rect.top=20

    def perp_level(self):
        level_str=str(self.stats.level)
        self.level_image=self.font.render(level_str,True,self.text_color,self.aliens_settings.bg_color)
        self.level_rect=self.level_image.get_rect()
        self.level_rect.right=self.screen_rect.right-10
        self.level_rect.bottom=self.ship.rect.top

    def perp_ships(self):
        self.ships=Group()
        for i in range(self.stats.ships_left):
            ship=Ship(self.screen,self.aliens_settings)
            ship.rect.left=10+i*(10+ship.rect.width)
            ship.rect.top=self.screen_rect.top
            self.ships.add(ship)

    def scoreboard_show(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.highest_score_image,self.highest_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.ships.draw(self.screen)
