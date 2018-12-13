import sys,pygame
from ship import Ship
from bullet import Bullet
from alien import Alien


def check_events(aliens_settings,screen,ship,bullets):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_events_keydown(event,ship,aliens_settings,screen,bullets)
        elif event.type==pygame.KEYUP:
            check_events_keyup(event,ship)

def check_events_keydown(event,ship,aliens_settings,screen,bullets):
    if event.key==pygame.K_q:
        sys.exit()
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

def get_number_aliens_x(aliens_settings,alien_width):
    available_space_x=aliens_settings.screen_width-2*alien_width
    number_aliens_x=int(available_space_x/(2*alien_width))
    return number_aliens_x

def get_number_rows(aliens_settings,ship_height,alien_height):
    available_space_y=(aliens_settings.screen_height-(3*alien_height)-ship_height)
    number_rows=int(available_space_y/(2*alien_height))
    return number_rows

def create_alien(aliens_settings,screen,aliens,alien_number,number_row):
    alien=Alien(aliens_settings,screen)
    alien_width=alien.rect.width
    alien.x=alien_width+2*alien_width*alien_number
    alien.rect.x=alien.x
    alien.rect.y=alien.rect.height+2*alien.rect.height*number_row
    aliens.add(alien)

def create_fleet(aliens_settings,screen,aliens,ship):
    alien=Alien(aliens_settings,screen)
    number_aliens_x=get_number_aliens_x(aliens_settings,alien.rect.width)
    number_rows=get_number_rows(aliens_settings,ship.rect.height,alien.rect.height)
    for alien_number in range(number_aliens_x):
        for number_row in range(number_rows):
            create_alien(aliens_settings,screen,aliens,alien_number,number_row)

def check_fleet_edges(aliens_settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_feet_direction(aliens_settings,aliens)
            break
def change_feet_direction(aliens_settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y+=aliens_settings.fleet_drop_speed
    aliens_settings.fleet_direction*=-1

def update_screen(aliens_settings,screen,ship,bullets,aliens):
    screen.fill(aliens_settings.bg_color)
    ship.update()
    ship.blitme()
    bullets.update()
    check_fleet_edges(aliens_settings,aliens)
    aliens.update()
    aliens.draw(screen)
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
    ship.fire_bullet(ship,bullets)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pygame.display.flip() #让最近绘制的屏幕可见
