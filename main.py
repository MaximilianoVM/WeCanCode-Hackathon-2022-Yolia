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

movil1 = Movil(372, 444, 'escultura')
movil2 = Movil(968, 444, 'estatua')

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
            Jugador.playerInput(event, player1, player2)

    if game_active:
        WIN.blit(fondo_surface, (0,0))

        text_surface = text_font.render('YOLIA', False, 'Black')
        text_rectangle = text_surface.get_rect(center = (WIDTH/2, 30))
        WIN.blit(text_surface, text_rectangle)

        WIN.blit(meta1.image, meta1.rect)
        WIN.blit(meta2.image, meta2.rect)

        WIN.blit(picos1.image, picos1.rect)
        WIN.blit(picos2.image, picos2.rect)

        WIN.blit(pared1.image, pared1.rect)
        WIN.blit(pared2.image, pared2.rect)

        WIN.blit(movil1.image, movil1.rect)
        WIN.blit(movil2.image, movil2.rect)

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
        
        if (player1.sprite.collision(movil1)):
            movil1.mover(pos_ant1)
        
        if (player2.sprite.collision(movil2)):
            movil2.mover(pos_ant2)


        # MANTENERLOS AL FINAL DEL CICLO
        player1.draw(WIN)
        player1.update()
        
        player2.draw(WIN)
        player2.update()
        
    else:
        WIN.blit(fondo_surface, (0,0))

    pygame.display.update()
    clock.tick(60)
