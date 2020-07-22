"""Contains all general settings for Alien Invasion"""
class Settings:
    """Class representing settings for Alien Invasion"""
    def __init__(self):
        """Initialize's Alien Invasion's settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.big_color = (240, 240, 240)

        # Ship attributes
        self.move_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings 
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # Fleet direction: 1 = Right // -1 = Left
        self.fleet_direction = 1
