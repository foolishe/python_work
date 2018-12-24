import sys,pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    pygame.init()
    aliens_settings=Settings()
    screen=pygame.display.set_mode((aliens_settings.screen_width,aliens_settings.screen_height))
    pygame.display.set_caption('Alien Incasion')
    ship=Ship(screen,aliens_settings)
    bullets=Group()
    aliens=Group()
    stats=GameStats(aliens_settings)
    sb=Scoreboard(aliens_settings,screen,stats,ship)
    play_button=Button(aliens_settings,screen,'PLAY')
    play_button.draw_button()
    pygame.display.flip()

    while True: #每次循环都会自动重绘屏幕
        gf.check_events(aliens_settings,screen,ship,bullets,play_button,stats,aliens,sb)
        if stats.game_active:
            ship.update()
            gf.update_aliens(aliens_settings,aliens,ship,stats,screen,bullets,sb)
            gf.update_bullets(aliens,bullets,screen,ship,aliens_settings,stats,sb)
            ship.fire_bullet(ship,bullets)
            gf.update_screen(aliens_settings,screen,
            ship,bullets,aliens,stats,play_button,sb)#屏幕更新就是画图不能涉及计算,不然画面会很卡.
run_game()
