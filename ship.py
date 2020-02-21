import pygame

class Ship():
    def __init__(self, screen, setting):
        self.screen = screen
        self.setting = setting

        #Draw ship
        self.image = pygame.image.load('pics/rocket.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.ship_start()

        #Check for direction 
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.speed = self.setting.ship_speed

    def ship_start(self):
        #Set ship position 
        self.rect.centerx = float(self.screen_rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.rect.centery = float(self.rect.centery)

    def blitting(self):
        #Draw the ship
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.rect.right < self.screen_rect.right and self.moving_right:
            self.rect.centerx += self.speed
        if self.rect.left > self.screen_rect.left and self.moving_left:
            self.rect.centerx -= self.speed
        if self.rect.top > self.screen_rect.top and self.moving_up:
            self.rect.centery -= self.speed
        if self.rect.bottom < self.screen_rect.bottom and self.moving_down:
            self.rect.centery += self.speed