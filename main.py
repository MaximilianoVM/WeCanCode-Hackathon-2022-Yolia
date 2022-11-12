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

fondo_surface = pygame.image.load('assets/HACKATHON FONDO TEMP.png').convert()

meta1 = Meta(52, 124)
meta2 = Meta(WIDTH - 52, HEIGHT -20)

player1 = pygame.sprite.GroupSingle()
player1.add(Jugador(576 - 32 + 20, 60 + 64, False, 'mexica'))

meta1 = Meta(20 + 32, 60 + 64)

while True: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        
    
    WIN.blit(fondo_surface, (0,0))

    WIN.blit(meta1.image, meta1.rect)
    player1.draw(WIN)

    pygame.display.update()
    clock.tick(60)
        