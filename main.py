import pygame
from sys import exit

pygame.init()

WIDTH, HEIGHT = 1212, 656
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("hackathon")
clock = pygame.time.Clock()

testSurface = pygame.image.load('assets/HACKATHON FONDO TEMP.png')

playerSurface = pygame.image.load('assets/Sprite-0006.png')


while True: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    WIN.blit(testSurface, (0,0))
    WIN.blit(playerSurface, (100,50))

    pygame.display.update()
    clock.tick(60)
        