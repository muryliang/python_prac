class Settings():
    """store alien invasion's settings"""

    def __init__(self):
        """initialize game setting"""
        #screen setting
        self.screen_width = 1024
        self.screen_height = 768
        self.bg_color = (230, 230, 230)

        #bullte set
        self.bullet_width = 3
        self.bullet_height = 5
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 10

        #alien
        self.fleet_drop_speed = 10
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()
        #ship
        self.ship_limit = 3

        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        self.fleet_direction = 1 
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print (self.alien_points)
