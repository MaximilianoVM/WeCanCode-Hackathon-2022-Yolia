import pygame 
from sys import exit 
from random import randint

class PLayer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/Sprite-0006.png').convert_alpha
        self.rect = self.image.get_rect(midbottom = (200,300))