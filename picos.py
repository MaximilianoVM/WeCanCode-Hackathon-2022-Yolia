import pygame

class Picos(pygame.sprite.Sprite):
    def __init__(self, x, y,tipo):
        super().__init__()

        self.x = x
        self.y = y

        self.frames = []
        self.frame_index = 0

        if tipo=='rosales': #rosales es un obtaculo del cielo que reduce vida 
            self.image.load('assets/rosales.png').convert_alpha()
        elif tipo=='enredadera':    #enredadera es obstaculo del mictlan que reduce vida 
            self.image.load('assets/Enredaderas/enredadera2.png').convert_alpha()
        


        self.rect = self.image.get_rect(midbottom = (self.x, self.y))