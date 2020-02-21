import pygame
from pygame.sprite import Sprite

class Heart(Sprite):
    def __init__(self, setting, screen):
        super().__init__()
        self.screen = screen
        self.setting = setting

        #Draw life
        self.image = pygame.image.load('pics/heart.png')
        self.rect = self.image.get_rect()

        #Set up position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height