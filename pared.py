import pygame

class Pared(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.x = x
        self.y = y

        self.image = pygame.image.load('assets/pared.jpg').convert_alpha() # Carga imagen
        self.image = pygame.transform.scale2x(self.image) # Escala imagen a 2x

        self.rect = self.image.get_rect(midbottom = (self.x, self.y)) # Define rectangulo 