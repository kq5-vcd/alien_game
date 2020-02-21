import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, setting, screen, ship):
        super().__init__()
        self.screen = screen

        #Create and set position 
        self.rect = pygame.Rect(0, 0, setting.bullet_width, setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.color = setting.bullet_color
        self.speed = setting.bullet_speed

    def update(self):
        self.rect.y -= self.speed

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)