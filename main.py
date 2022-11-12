import pygame
from jugador import Jugador
from pared import Pared
from meta import Meta
from sys import exit

pygame.init()

#=================== DALTONISMO SI O NO ===================#
dalt = False
#==========================================================#

WIDTH, HEIGHT = 1212, 656
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("YOLIA")
clock = pygame.time.Clock()
testFont = pygame.font.SysFont("comicsans", 50)

game_active = False
start_time = 0

#=================== GRUPOS
jugador_group = pygame.sprite.GroupSingle()
jugador_group.add(Jugador(100, 100, dalt, 'mexica'))

testSurface = pygame.image.load('assets/HACKATHON FONDO TEMP.png').convert()

playerSurface = pygame.image.load('assets/Sprite-0006.png').convert_alpha()

player1 = pygame.sprite.GroupSingle()
player1.add( Jugador(100, 100, False, 'mexica') )

meta1 = Meta(20 + 32, 60 + 64)

while True: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        
    
    WIN.blit(testSurface, (0,0))
    WIN.blit(playerSurface, (100,50))
    WIN.blit(meta1.image, meta1.rect)
    player1.draw(WIN)

    pygame.display.update()
    clock.tick(60)
        