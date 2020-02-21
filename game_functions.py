import sys
import pygame
from random import randint
from time import sleep

from bullet import Bullet
from alien import Alien

from heart import Heart
from star import Star
from button import Button

#Keyboard functions
def check_key_down(ship, event, setting, screen, bullets, stats, button):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    
    if event.key == pygame.K_f:
        if ship.speed < 5:
            ship.speed += .5
    if event.key == pygame.K_s:
        if ship.speed > .5:
            ship.speed -= .5
    
    if event.key == pygame.K_SPACE:
        fire(setting, screen, ship, bullets)
        
    if event.key == pygame.K_q:
        sys.exit()
    
    if event.key == pygame.K_a:
        if stats.lives > 0:
            stats.active = True
            pygame.mouse.set_visible(False)
    
    if event.key == pygame.K_p:
        button.prep_msg("resume".upper())
        stats.active = False
        pygame.mouse.set_visible(True)

def check_key_up(ship, event):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(ship, setting, screen, score, level, bullets, stats, button, lives):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down(ship, event, setting, screen, bullets, stats, button)
        elif event.type == pygame.KEYUP:
            check_key_up(ship, event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            check_button(setting, screen, stats, score, level, lives, button, x, y)
            
#Update functions
def update_screen(setting, screen, stats, score, level, ship, bullets, aliens, stars, lives, button):
    screen.fill(setting.rbg_color)

    stars.draw(screen)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitting()
    #All aliens will be drawn with draw()
    aliens.draw(screen)

    lives.draw(screen)
    score.show_score()
    level.display_level()

    if not stats.active:
        if stats.lives <= 0:
            score.show_high_score()
            button.prep_msg("new game".upper())

            setting.initialize_dynamic_settings()
            ship.speed = setting.ship_speed

        button.draw_button()

    #Update screen animation
    pygame.display.flip()

def next_level(setting, stats, level):
    stats.level += 1
    level.prep_level()

    setting.alien_speed += .5

    setting.bullet_speed = randint(1, 7)
    setting.bullet_width = randint(2, 8)
    setting.bullet_height = randint(5, 20)

#Button functions
def check_button(setting, screen, stats, score, level, lives, button, x, y):
    if button.rect.collidepoint(x, y) and not stats.active:
        #Hide the mouse
        pygame.mouse.set_visible(False)

        #Reset game
        if stats.lives <= 0:
            stats.reset_stats()
            set_lives(setting, screen, stats, lives)

            score.prep_score()
            score.show_score()

            level.prep_level()
            level.display_level()

        stats.active = True

#Lives function
def set_lives(setting, screen, stats, lives):
    life = Heart(setting, screen)
    width = life.rect.width
    height = life.rect.height

    for num in range(stats.lives):
        make_life(setting, screen, lives, width + 2 * width * num, height)

def make_life(setting, screen, lives, x, y):
    #Set up
    life = Heart(setting, screen)
    
    #Set position
    life.rect.x = x
    life.rect.y = y

    lives.add(life)

def remove_life(lives):
    arr = [life for life in lives]
    lives.remove(arr[-1])

#Ship functions
def ship_hit(setting, stats, score, screen, ship, aliens, bullets, lives):
        if stats.lives > 0:
            #Reset game
            stats.lives -= 1
            remove_life(lives)

            aliens.empty()
            bullets.empty()

            create_fleet(setting, screen, aliens, ship)
            ship.ship_start()

            if stats.lives == 0:
                stats.active = False
                pygame.mouse.set_visible(True)

            #Pause game
            sleep(0.5)
        else:
            stats.active = False
            pygame.mouse.set_visible(True)

#Bullet functions
def update_bullets(bullets, aliens, setting, screen, ship, stats, score, level):
    #Calling method on Group will call it on each element of the group
    bullets.update()

    #Elements in a Group cannot be removed directly in the loop
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_collision(setting, screen, stats, score, level, ship, aliens, bullets)

def fire(setting, screen, ship, bullets):
    if len(bullets) < setting.inventory:
        new_bullet = Bullet(setting, screen, ship)
        bullets.add(new_bullet)

#Alien functions
def create_alien(setting, screen, aliens, line_position, row_number):
    #Set up
    alien = Alien(setting, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    
    #Set position
    alien.rect.x = alien_width + 2 * alien_width * line_position
    alien.rect.y = alien_height + 2 * alien_height * row_number + 10

    aliens.add(alien)

def get_line_quantity(setting, alien_width):
    #Return number of aliens in each row
    available_space_x = setting.screen_width - alien_width * 2
    quantity = int(available_space_x / (2 * alien_width))

    return quantity

def get_row_quantity(setting, alien_height, ship_height):
    #Return number of alien rows
    available_space_y = setting.screen_height - alien_height * 3 - ship_height
    rows = int(available_space_y / (2 * alien_height))

    return rows

def create_fleet(setting, screen, aliens, ship):
    #Temp alien for measurement
    alien = Alien(setting, screen)
    alien_quantity = get_line_quantity(setting, alien.rect.width)
    rows = get_row_quantity(setting, alien.rect.height, ship.rect.height)
    
    #Fleet
    for row in range(rows):
        for alien_num in range(alien_quantity):
            create_alien(setting, screen, aliens, alien_num, row)

def update_aliens(setting, stats, screen, score, aliens, ship, bullets, lives):
    #Check for ship collision
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(setting, stats, score, screen, ship, aliens, bullets, lives)
    
    #Check for change of direction
    check_fleet_edges(setting, aliens)
    check_rock_bottom(setting, stats, screen, score, ship, aliens, bullets, lives)
    aliens.update()

def check_fleet_edges(setting, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_dir(setting, aliens)
            break

def change_fleet_dir(setting, aliens):
    for alien in aliens.sprites():
        alien.rect.y += setting.alien_drop
    setting.alien_dir *= -1

def check_collision(setting, screen, stats, score, level, ship, aliens, bullets):
    #Check for collision
    #True checks if the object should be destroyed
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    #collisions is a dictionary containing aliens shot by a bullet
    if collisions:
        for aliens in collisions.values():
            stats.score += setting.reward * stats.level * len(aliens)
            score.prep_score()
            
            if stats.score > stats.high_score:
                stats.high_score = stats.score
                score.prep_high_score()

    if len(aliens) == 0:
        #Reset to new level
        bullets.empty()
        next_level(setting, stats, level)

        create_fleet(setting, screen, aliens, ship)

def check_rock_bottom(setting, stats, screen, score, ship, aliens, bullets, lives):
    screen_rect = screen.get_rect()

    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(setting, stats, score, screen, ship, aliens, bullets, lives)
            break

#Stars
def update_stars(setting, stars, screen):
    if len(stars) == 0:
        for num in range(42):
            x = randint(0, setting.screen_width)
            y = randint(0, setting.screen_height)
            new_star = Star(setting, screen, x, y)
            stars.add(new_star)

    stars.update()

    for star in stars.copy():
        if star.rect.bottom > setting.screen_height:
            stars.remove(star)

            x = randint(0, setting.screen_width)
            new_star = Star(setting, screen, x, 0)
            stars.add(new_star)