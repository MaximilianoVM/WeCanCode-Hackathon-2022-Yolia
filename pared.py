import pygame

class Pared(pygame.sprite.Sprite):
    def __init__(self, x, y,mundo):
        super().__init__()

        self.x = x
        self.y = y

        if mundo=='estatua': #estatua es un obtaculo del cielo que reduce vida 
            self.image.load('assets/nuves.png').convert_alpha()
            self.image = pygame.transform.scale2x(self.image) # Escala imagen a 2x
        elif mundo=='escultura': #escultura es obstaculo del mictlan que reduce vida 
            self.image.load('assets/piedras.png').convert_alpha()
            self.image = pygame.transform.scale2x(self.image) # Escala imagen a 2x

        self.rect = self.image.get_rect(midbottom = (self.x, self.y)) # Define rectangulo 