import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from score import Score
from level import Level

import game_functions as game

def run_game():
    #Set gaming window
    pygame.init()
    default_setting = Settings()
    screen = pygame.display.set_mode(default_setting.screen_size)
    pygame.display.set_caption("Alien Invasion")

    stats = GameStats(default_setting)
    score = Score(default_setting, screen, stats)
    level = Level(default_setting, screen, stats)
    play = Button(default_setting, screen, "play".upper())

    ship = Ship(screen, default_setting)
    #Create a groups to manage
    bullets = Group()
    aliens = Group()
    stars = Group()
    lives = Group()
    game.set_lives(default_setting, screen, stats, lives)

    game.create_fleet(default_setting, screen, aliens, ship)

    while True:
        #Check keyboard
        game.check_events(ship, default_setting, screen, score, level, bullets, stats, play, lives)
        
        if stats.active:
            game.update_stars(default_setting, stars, screen)
            ship.update()
            game.update_bullets(bullets, aliens, default_setting, screen, ship, stats, score, level)
            game.update_aliens(default_setting, stats, screen, score, aliens, ship, bullets, lives)
        
        game.update_screen(default_setting, screen, stats, score, level, ship, bullets, aliens, stars, lives, play)

run_game()