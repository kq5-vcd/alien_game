import pygame
from pygame.sprite import Sprite
from random import randint

class Star(Sprite):
    def __init__(self, setting, screen, x, y):
        super().__init__()
        self.screen = screen
        self.setting = setting

        #Draw star
        self.image = pygame.image.load('pics/star.png')
        self.rect = self.image.get_rect()

        #Set up  position
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y += 2