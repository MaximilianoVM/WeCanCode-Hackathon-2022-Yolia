import pygame
from jugador import Jugador
from pared import Pared
from meta import Meta
from picos import Picos
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

pygame.mixer.init()
pygame.mixer.music.load("music/musica.wav")
pygame.mixer.music.play(-1)

game_active = True
start_time = 0

#=================== GRUPOS
player1 = pygame.sprite.GroupSingle()
player1.add(Jugador(False, 'mexica'))

player2 = pygame.sprite.GroupSingle()
player2.add(Jugador(False, 'cristiano'))

fondo_surface = pygame.image.load('assets/Fondos/FondoBien.png').convert()
fondo_surface = pygame.transform.scale2x(fondo_surface)

meta1 = Meta(52, 124)
meta2 = Meta(648, 124)

picos1 = Picos(52 + 64 + 64, 124, 'enredadera')
picos2 = Picos(648 + 64, 124, 'rosales')

pared1 = Pared(52 + 64, 124 + 64 + 64 + 64, 'piedra')
pared2 = Pared(648 + 64 + 64, 124 + 64 + 64, 'hoyo')

contador_fin = 0

llego = False

while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if (event.type == pygame.KEYDOWN and llego == False):
            pos_ant1 = (player1.sprite.rect.x, player1.sprite.rect.y)
            pos_ant2 = (player2.sprite.rect.x, player2.sprite.rect.y)
            Jugador.playerInput(player1, event, player1, player2, WIDTH, HEIGHT)
            print(player2.sprite.rect.y)
            print(player2.sprite.rect.x)

    if game_active:
        WIN.blit(fondo_surface, (0,0))

        WIN.blit(meta1.image, meta1.rect)
        WIN.blit(meta2.image, meta2.rect)

        WIN.blit(picos1.image, picos1.rect)
        WIN.blit(picos2.image, picos2.rect)

        WIN.blit(pared1.image, pared1.rect)
        WIN.blit(pared2.image, pared2.rect)

        if (player1.sprite.llega_meta(meta1) and player2.sprite.llega_meta(meta2)):
            llego = True
            contador_fin += 1

            if contador_fin == 30:
                game_active = False
        
        if (player1.sprite.collision(picos1) or player2.sprite.collision(picos2)):
            player1.sprite.restart()
            player2.sprite.restart()

        if (player1.sprite.collision(pared1)):
            player1.sprite.rect.x = pos_ant1[0]
            player1.sprite.rect.y = pos_ant1[1]
        
        if (player2.sprite.collision(pared2)):
            player2.sprite.rect.x = pos_ant2[0]
            player2.sprite.rect.y = pos_ant2[1]

        # MANTENERLOS AL FINAL DEL CICLO
        player1.draw(WIN)
        player1.update()
        
        player2.draw(WIN)
        player2.update()
        
    else:
        WIN.blit(fondo_surface, (0,0))

    pygame.display.update()
    clock.tick(60)
