import pygame

class Jugador:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def dibujar(self, superficie):
        pygame.draw.rect(superficie, (self.x, self.y))