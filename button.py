#Render text to the screen
import pygame.font 

class Button():
    def __init__(self, setting, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #Set button properties
        self.width, self.height = 200, 50
        self.color = (10, 20, 255)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        #Build button
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center 

        self.prep_msg(msg)

    def prep_msg(self, msg):
        #Turn text into an image and render it
        self.msg_img = self.font.render(msg, True, self.text_color, self.color)
        self.msg_rect = self.msg_img.get_rect()
        self.msg_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.color, self.rect)
        self.screen.blit(self.msg_img, self.msg_rect)