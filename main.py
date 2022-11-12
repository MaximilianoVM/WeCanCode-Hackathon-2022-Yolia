import pygame
from jugador import Jugador
from pared import Pared
from meta import Meta
from sys import exit

pygame.init()

WIDTH, HEIGHT = 1212, 656
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("YOLIA")
clock = pygame.time.Clock()

testSurface = pygame.image.load('assets/HACKATHON FONDO TEMP.png').convert()

playerSurface = pygame.image.load('assets/Sprite-0006.png').convert_alpha()

meta1 = Meta(20 + 32, 60 + 64)

while True: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        
    
    WIN.blit(testSurface, (0,0))
    WIN.blit(playerSurface, (100,50))
    WIN.blit(meta1.image, meta1.rect)

    pygame.display.update()
    clock.tick(60)
        