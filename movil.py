import pygame

class Picos(pygame.sprite.Sprite):
    def __init__(self, x, y,tipo):
        super().__init__()

        self.x = x
        self.y = y

        self.frames = []
        self.frame_index = 0

        if tipo=='estatua': #estatua es un obtaculo del cielo que reduce vida 
            self.image.load('assets/Estatuas/estatua.png').convert_alpha()
        elif tipo=='escultura': #escultura es obstaculo del mictlan que reduce vida 
            self.image.load('assets/escultura.png').convert_alpha()
        

        self.rect = self.image.get_rect(midbottom = (self.x, self.y))

    def collision(self, other):
        if self.rect.colliderect(other.rect):return True
        else: return False
