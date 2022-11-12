import pygame

class Picos(pygame.sprite.Sprite):
    def __init__(self, x, y,tipo):
        super().__init__()

        self.x = x
        self.y = y

        self.frames = []
        self.frame_index = 0

        if tipo=='rosales':
            self.image = pygame.image.load('assets/Rosales/rosales.png').convert_alpha() # Carga imagen
            self.image = pygame.transform.scale2x(self.image) # Escala imagen a 2x
        elif tipo=='enredadera':
            self.image = pygame.image.load('assets/Enredaderas/enredadera2.png').convert_alpha() # Carga imagen
            self.image = pygame.transform.scale2x(self.image) # Escala imagen a 2x
        
        #self.image = pygame.image.load('assets/Sprite-0006.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = (self.x, self.y))