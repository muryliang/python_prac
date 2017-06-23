import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """manage bullet shoot from ship"""

    def __init__(self, ai_settings, screen, ship):
        """create a bullet at the place of ship"""
        super().__init__()
        self.screen = screen

        # create a bullet on (0,0) then modify place
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #store place bullet
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """move up bullet"""
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """draw bullet on screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
