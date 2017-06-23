import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """represent alien class"""

    def __init__(self, ai_settings, screen):
        """initialize alien, set origin pos"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #load image , set pos
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #alien initial place is left top
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        """move right or left"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """if at edges, return True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True


