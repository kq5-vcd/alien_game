import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, setting, screen):
        super().__init__()
        self.screen = screen
        self.setting = setting

        #Draw alien ship
        self.image = pygame.image.load('pics/ufo.png')
        self.rect = self.image.get_rect()

        #Set up  position
        self.rect.x = float(self.rect.width)
        self.rect.y = float(self.rect.height)

    def update(self):
        self.rect.x += (self.setting.alien_speed * self.setting.alien_dir)

    def check_edges(self):
        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True