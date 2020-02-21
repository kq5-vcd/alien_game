import pygame.font 

class Score():
    def __init__(self, setting, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.setting = setting
        self.stats = stats

        #Font setting
        self.text_color = (200, 200, 200)
        self.font = pygame.font.SysFont(None, 50)

        #Prepare the initial score image
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        #Render score with format
        score = "{:,}".format(self.stats.score)
        self.score_img = self.font.render(score, True, self.text_color, self.setting.rbg_color)

        #Display score
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        #Render score with format
        high_score = "BEST: " + "{:,}".format(self.stats.score)
        self.high_score_img = self.font.render(high_score, True, self.text_color, self.setting.rbg_color)

        #Display score
        self.high_score_rect = self.high_score_img.get_rect()
        self.high_score_rect.left = 20
        self.high_score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_img, self.score_rect)

    def show_high_score(self):
        self.screen.blit(self.high_score_img, self.high_score_rect)