import pygame
from jugador import Jugador
from pared import Pared
from meta import Meta
from picos import Picos
from movil import Movil
from sys import exit

pygame.init()

#=================== DALTONISMO SI O NO ===================#
dalt = False
#==========================================================#

WIDTH, HEIGHT = 1212, 656
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("YOLIA")

clock = pygame.time.Clock()

text_font = pygame.font.Font('fonts/I-pixel-u.ttf', 64)

pygame.mixer.init()
pygame.mixer.music.load("music/musica.wav")
pygame.mixer.music.play(-1)

game_active = True
start_time = 0

#=================== GRUPOS
#PLAYERS
player1 = pygame.sprite.GroupSingle()
player1.add(Jugador(False, 'mexica'))

player2 = pygame.sprite.GroupSingle()
player2.add(Jugador(False, 'cristiano'))

#FONDOS
fondo_surface = pygame.image.load('assets/Fondos/FondoBien.png').convert()
fondo_surface = pygame.transform.scale2x(fondo_surface)

#METAS
meta1 = Meta(52, 124)
meta2 = Meta(648, 124)

#PICOS
picos = pygame.sprite.Group()
picos.add(Picos(52 + 64 + 64, 124, 'enredadera'))
picos.add(Picos(648 + 64, 124, 'rosales'))

#PAREDES
paredes = pygame.sprite.Group()
paredes.add(Pared(52 + 64, 124 + 64 + 64 + 64, 'piedra'))
paredes.add(Pared(648 + 64 + 64, 124 + 64 + 64, 'hoyo'))

#===================#

movil1 = Movil(372, 444, 'escultura')
movil2 = Movil(968, 444, 'estatua')

contador_fin = 0

llego = False

while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        #DETECTAR TECLAS
        if (event.type == pygame.KEYDOWN and llego == False):
            pos_ant1 = (player1.sprite.rect.x, player1.sprite.rect.y)
            pos_ant2 = (player2.sprite.rect.x, player2.sprite.rect.y)
            Jugador.playerInput(event, player1, player2)

    if game_active:

        #IMPRIME FONDO
        WIN.blit(fondo_surface, (0,0))
        
        #IMPRIME METAS
        WIN.blit(meta1.image, meta1.rect)
        WIN.blit(meta2.image, meta2.rect)

        #DIBUJA PICOS
        picos.draw(WIN)

        #DIBUJA PAREDES
        paredes.draw(WIN)

        #DETECTA SI LLEGA A LA META
        if (player1.sprite.llega_meta(meta1) and player2.sprite.llega_meta(meta2)):
            llego = True
            contador_fin += 1

            if contador_fin == 30:
                game_active = False

        #=================== COLISION CON PICOS

        for i in range (len(picos)):
            if(player1.sprite.rect.colliderect(picos.sprites()[i].rect) or player2.sprite.rect.colliderect(picos.sprites()[i].rect)):
                player1.sprite.restart()
                player2.sprite.restart()

        #=================== COLISION CON PARED

        for i in range (len(paredes)):
            if(player1.sprite.rect.colliderect(paredes.sprites()[i].rect)):
                player1.sprite.rect.x = pos_ant1[0]
                player1.sprite.rect.y = pos_ant1[1]
            
            if(player2.sprite.rect.colliderect(paredes.sprites()[i].rect)):
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
