import pygame

class Picos(pygame.sprite.Sprite):
    def __init__(self, x, y,tipo):
        super().__init__()

        self.x = x
        self.y = y

        if tipo=='estatua': #estatua es un obtaculo del cielo que reduce vida 
            self.image = pygame.image.load('assets/Estatuas/estatua.png').convert_alpha() # Carga imagen
            self.image = pygame.transform.scale2x(self.image) # Escala imagen a 2x

        elif tipo=='escultura': #escultura es obstaculo del mictlan que reduce vida 
            self.image = pygame.image.load('assets/Escultura/escultura.png').convert_alpha() # Carga imagen
            self.image = pygame.transform.scale2x(self.image) # Escala imagen a 2x

        self.rect = self.image.get_rect(midbottom = (self.x, self.y))

    def collision(self, other):
        if self.rect.colliderect(other.rect):return True
        else: return False
