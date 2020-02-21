class Settings():
    def __init__(self):
        #Screen
        self.screen_width = 1080
        self.screen_height = 720
        self.screen_size = (self.screen_width, self.screen_height)
        self.rbg_color = (20, 150, 222)

        #Ship:
        self.lives = 3
        self.inventory = 20

        #Bullet
        self.bullet_color = (50, 50, 50)

        #Alien
        self.alien_drop = 5
        
        #Stats
        self.level = 1
        self.reward = 10

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        #Create props that will be changed
        #Ship
        self.ship_speed = 1

        #Bullet
        self.bullet_speed = 4
        self.bullet_width = 3
        self.bullet_height = 10
        
        #Alien
        self.alien_dir = 1
        self.alien_speed = 1