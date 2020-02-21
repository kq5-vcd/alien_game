class GameStats():
    def __init__(self, setting):
        self.setting = setting

        #Initiate the function immediately
        self.reset_stats()
        self.active = False

        self.high_score = 0

    def reset_stats(self):
        self.lives = self.setting.lives
        self.level = self.setting.level
        self.score = 0