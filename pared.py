import pygame

class Pared(pygame.sprite.Sprite):
    def __init__(self, x, y, tipo):
        super().__init__()

        self.x = x
        self.y = y

        if tipo == 'hoyo':
            self.image = pygame.image.load('assets/Hoyo/HoyoNube.png').convert_alpha() # Carga imagen
            self.image = pygame.transform.scale2x(self.image) # Escala imagen a 2x
            
        elif tipo == 'piedra':
            self.image = pygame.image.load('assets/Piedras/piedra.png').convert_alpha() # Carga imagen
            self.image = pygame.transform.scale2x(self.image) # Escala imagen a 2x

        self.rect = self.image.get_rect(midbottom = (self.x, self.y)) # Define rectangulo 