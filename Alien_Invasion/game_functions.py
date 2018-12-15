import sys,pygame,time
from ship import Ship
from bullet import Bullet
from alien import Alien


def check_events(aliens_settings,screen,ship,bullets,play_button,stats,aliens):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_events_keydown(event,ship,aliens_settings,screen,bullets)
        elif event.type==pygame.KEYUP:
            check_events_keyup(event,ship)
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_button(stats,play_button,mouse_x,mouse_y,aliens_settings,aliens,ship,bullets,screen)

def check_play_button(stats,play_button,mouse_x,mouse_y,aliens_settings,aliens,ship,bullets,screen):
    if play_button.rect.collidepoint(mouse_x,mouse_y):
        aliens_settings.speed_factor()
        aliens.empty()
        bullets.empty()
        create_fleet(aliens_settings,screen,aliens,ship)
        ship.center_ship()
        time.sleep(0.5)
        stats.game_active=True
        stats.score=0
        pygame.mouse.set_visible(False)



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

def ship_hit(aliens_settings,stats,screen,ship,aliens,bullets):
    if stats.ships_left>0:
        stats.ships_left-=1
        aliens.empty()
        bullets.empty()
        create_fleet(aliens_settings,screen,aliens,ship)
        ship.center_ship()
        time.sleep(0.5)
    else:
         stats.game_active=False
         pygame.mouse.set_visible(True)

def update_bullets(aliens,bullets,screen,ship,aliens_settings,stats,sb):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
    collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)
    if collisions:
        for alien in collisions.values():
            stats.score+=aliens_settings.alien_point*len(alien)
            sb.perp_score()
    if len(aliens)==0:
        aliens_settings.speed_increase()
        bullets.empty()
        create_fleet(aliens_settings,screen,aliens,ship)

def update_aliens(aliens_settings,aliens,ship,stats,screen,bullets):
    check_fleet_edges(aliens_settings,aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens) or check_aliens_bottom(screen,aliens):
        ship_hit(aliens_settings,stats,screen,ship,aliens,bullets)

def check_aliens_bottom(screen,aliens):
    for alien in aliens.sprites():
        if alien.rect.bottom>=screen.get_rect().bottom:
            return True

def update_screen(aliens_settings,screen,ship,bullets,aliens,stats,play_button,sb):
    screen.fill(aliens_settings.bg_color)
    ship.blitme()
    aliens.draw(screen)
    sb.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip() #让最近绘制的屏幕可见
