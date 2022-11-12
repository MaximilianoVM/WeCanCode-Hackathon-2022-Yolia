import pygame

class Picos(pygame.sprite.Sprite):
    def __init__(self, x, y,tipo):
        super().__init__()

        self.x = x
        self.y = y

        self.frames = []
        self.frame_index = 0

        if tipo=='rosales': #rosales es un obtaculo que reduce vida del cielo
            self.image.load('assets/rosales.png').convert_alpha()
        elif tipo=='enredadera':    #enredadera es obstaculo que reduce vida del mictlan
            self.image.load('assets/Enredaderas/enredadera2.png').convert_alpha()
        

        #self.image = pygame.image.load('assets/Sprite-0006.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = (self.x, self.y))



    def collision(self, other):
         return self.rect.colliderect(other.rect)


