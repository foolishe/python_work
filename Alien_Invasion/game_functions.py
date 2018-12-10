import sys,pygame
from ship import Ship
from bullet import Bullet


def check_events(aliens_settings,screen,ship,bullets):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_events_keydown(event,ship,aliens_settings,screen,bullets)
        elif event.type==pygame.KEYUP:
            check_events_keyup(event,ship)

def check_events_keydown(event,ship,aliens_settings,screen,bullets):
    if event.key==pygame.K_SPACE:
        ship.fire=True
    if event.key==pygame.K_RIGHT:
        ship.moving_right=True
    if event.key==pygame.K_LEFT:
        ship.moving_left=True

def check_events_keyup(event,ship):
    if event.key==pygame.K_SPACE:
        ship.fire=False
        ship.bullet_time=0
    if event.key==pygame.K_RIGHT:
        ship.moving_right=False
    if event.key==pygame.K_LEFT:
        ship.moving_left=False

def update_screen(aliens_settings,screen,ship,bullets):
    screen.fill(aliens_settings.bg_color)
    ship.update()
    ship.blitme()
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
    ship.fire_bullet(ship,bullets)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pygame.display.flip() #让最近绘制的屏幕可见
