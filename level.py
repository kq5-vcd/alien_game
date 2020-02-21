import pygame.font 

class Level():
    def __init__(self, setting, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.setting = setting
        self.stats = stats

        #Font setting
        self.text_color = (100, 100, 100)
        self.font = pygame.font.SysFont(None, 50)

        #Prepare the initial level image
        self.prep_level()

    def prep_level(self):
        #Render level with format
        level = "LEVEL " + str(self.stats.level)
        self.lvl_img = self.font.render(level, True, self.text_color, self.setting.rbg_color)

        #Display level
        self.lvl_rect = self.lvl_img.get_rect()
        self.lvl_rect.centerx = self.screen_rect.centerx
        self.lvl_rect.top = 20

    def display_level(self):
        self.screen.blit(self.lvl_img, self.lvl_rect)