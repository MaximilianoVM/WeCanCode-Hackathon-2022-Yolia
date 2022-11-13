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
menu = True
#==========================================================#


WIDTH, HEIGHT = 1212, 656
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("YOLIA")

clock = pygame.time.Clock()

text_font = pygame.font.Font('fonts/I-pixel-u.ttf', 64)

pygame.mixer.init()
pygame.mixer.music.load("music/musica.wav")
pygame.mixer.music.play(-1)

start_time = 0

#=================== GRUPOS
#PLAYERS
player1 = pygame.sprite.GroupSingle()
player1.add(Jugador(dalt, 'mexica'))

player2 = pygame.sprite.GroupSingle()
player2.add(Jugador(dalt, 'cristiano'))

#FONDOS
fondo_surface = pygame.image.load('assets/Fondos/FondoMarco.png').convert()
fondo_surface = pygame.transform.scale2x(fondo_surface)

#MENU
titulo_surface = pygame.image.load("assets/fondo.png").convert()
nombre_surface = pygame.image.load("assets/Titulo.png").convert()
nombre_surface = pygame.transform.scale2x(nombre_surface)

##==========================================BORRAR POR SI ACASO=================================================#
while menu == True:
        
    #create menu
    WIN.blit(titulo_surface, (0,0))
    WIN.blit(nombre_surface, (200,50))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                menu = False
                game_active = True
                nivel = 1
                break
            if event.key == pygame.K_d:
                dalt = True
                menu = False
                game_active = True
                nivel = 1
                break

##===========================================================================================#

#METAS FALSAS
meta1 = Meta(-64, -64)
meta2 = Meta(-64, -64)

#PAREDES FALSAS
paredes = pygame.sprite.Group()

#PICOS FALSOS 
picos = pygame.sprite.Group()

#MOVILES FALSOS
movil1 = Movil(-64, -64, 'escultura')
movil2 = Movil(-64, -64, 'estatua')

nivel = 0
game_active = False
contador_fin = 0
llego = False

WIN.blit(nombre_surface, (200,50))

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

        #IMPRIME MOVILES
        WIN.blit(movil1.image, movil1.rect)
        WIN.blit(movil2.image, movil2.rect)

        #EMPUJAR MOVILES
        if(player1.sprite.collision(movil1)):
            movil1.mover(pos_ant1)

            if (player1.sprite.rect.x + 64 > 532 or player1.sprite.rect.x - 64 < 20):
                player1.sprite.rect.x = pos_ant1[0]
            if (player1.sprite.rect.y + 64 > 572 or player1.sprite.rect.y - 64 < 60):
                player1.sprite.rect.y = pos_ant1[1]

        if(player2.sprite.collision(movil2)):
            movil2.mover(pos_ant2)

            if (player2.sprite.rect.x + 64 > 1128 or player2.sprite.rect.x - 64 < 616):
                player2.sprite.rect.x = pos_ant2[0]
            if (player2.sprite.rect.y + 64 > 572 or player2.sprite.rect.y - 64 < 60):
                player2.sprite.rect.y = pos_ant2[1]
                

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
                movil1.reiniciar()
                player2.sprite.restart()
                movil2.reiniciar()

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

        text_font = pygame.font.Font('fonts/I-pixel-u.ttf', 60)
        text_surface = text_font.render('YOLIA', False, 'Black')

        text_rectangle = text_surface.get_rect(center = (WIDTH/2, 25))
        WIN.blit(text_surface, text_rectangle)

    else:
        game_active = True
        nivel += 1
        contador_fin = 0
        llego = False

        #PLAYERS
        player1.remove(player1.sprite)
        player2.remove(player2.sprite)
        
        player1.add(Jugador(dalt, 'mexica'))
        player2.add(Jugador(dalt, 'cristiano'))

        if nivel == 1:
            #METAS
            meta1 = Meta(20 + (64 * 8) - 32, 60 + (64 * 9))

            meta2 = Meta(616 + (64 * 8) - 32, 60 + (64 * 9))

        if nivel == 2:
            #METAS
            meta1 = Meta(20 + (64 * 2) - 32, 60 + (64 * 2))

            meta2 = Meta(616 + (64 * 9) - 32, 60 + (64 * 1))

            #PAREDES
            paredes.empty()
            paredes.add(Pared(20 + (64 * 4) - 32, 60 + (64 * 5), 'piedra'))
            paredes.add(Pared(20 + (64 * 4) - 32, 60 + (64 * 6), 'piedra'))
            paredes.add(Pared(20 + (64 * 5) - 32, 60 + (64 * 6), 'piedra'))
            paredes.add(Pared(20 + (64 * 6) - 32, 60 + (64 * 6), 'piedra'))
            paredes.add(Pared(20 + (64 * 6) - 32, 60 + (64 * 5), 'piedra'))
            paredes.add(Pared(20 + (64 * 2) - 32, 60 + (64 * 1), 'piedra'))
            paredes.add(Pared(20 + (64 * 1) - 32, 60 + (64 * 2), 'piedra'))

            paredes.add(Pared(616 + (64 * 4) - 32, 60 + (64 * 5), 'hoyo'))
            paredes.add(Pared(616 + (64 * 4) - 32, 60 + (64 * 4), 'hoyo'))
            paredes.add(Pared(616 + (64 * 5) - 32, 60 + (64 * 4), 'hoyo'))
            paredes.add(Pared(616 + (64 * 6) - 32, 60 + (64 * 4), 'hoyo'))
            paredes.add(Pared(616 + (64 * 6) - 32, 60 + (64 * 5), 'hoyo'))
            paredes.add(Pared(616 + (64 * 8) - 32, 60 + (64 * 4), 'hoyo'))
            paredes.add(Pared(616 + (64 * 8) - 32, 60 + (64 * 1), 'hoyo'))

        if nivel == 3:
            #METAS
            meta1 = Meta(20 + (64 * 2) - 32, 60 + (64 * 2))

            meta2 = Meta(616 + (64 * 8) - 32, 60 + (64 * 8))

            #PAREDES
            paredes.empty()
            paredes.add(Pared(20 + (64 * 4) - 32, 60 + (64 * 6), 'piedra'))
            paredes.add(Pared(20 + (64 * 4) - 32, 60 + (64 * 7), 'piedra'))
            paredes.add(Pared(20 + (64 * 4) - 32, 60 + (64 * 8), 'piedra'))
            paredes.add(Pared(20 + (64 * 4) - 32, 60 + (64 * 9), 'piedra'))
            paredes.add(Pared(20 + (64 * 5) - 32, 60 + (64 * 4), 'piedra'))
            paredes.add(Pared(20 + (64 * 6) - 32, 60 + (64 * 6), 'piedra'))
            paredes.add(Pared(20 + (64 * 6) - 32, 60 + (64 * 3), 'piedra'))
            paredes.add(Pared(20 + (64 * 6) - 32, 60 + (64 * 2), 'piedra'))
            paredes.add(Pared(20 + (64 * 3) - 32, 60 + (64 * 2), 'piedra'))
            paredes.add(Pared(20 + (64 * 1) - 32, 60 + (64 * 4), 'piedra'))

            paredes.add(Pared(616 + (64 * 4) - 32, 60 + (64 * 4), 'hoyo'))
            paredes.add(Pared(616 + (64 * 4) - 32, 60 + (64 * 3), 'hoyo'))
            paredes.add(Pared(616 + (64 * 4) - 32, 60 + (64 * 2), 'hoyo'))
            paredes.add(Pared(616 + (64 * 6) - 32, 60 + (64 * 4), 'hoyo'))
            paredes.add(Pared(616 + (64 * 6) - 32, 60 + (64 * 1), 'hoyo'))
            paredes.add(Pared(616 + (64 * 1) - 32, 60 + (64 * 6), 'hoyo'))
            paredes.add(Pared(616 + (64 * 2) - 32, 60 + (64 * 6), 'hoyo'))
            paredes.add(Pared(616 + (64 * 3) - 32, 60 + (64 * 6), 'hoyo'))
            paredes.add(Pared(616 + (64 * 7) - 32, 60 + (64 * 5), 'hoyo'))
            paredes.add(Pared(616 + (64 * 6) - 32, 60 + (64 * 6), 'hoyo'))
            paredes.add(Pared(616 + (64 * 8) - 32, 60 + (64 * 3), 'hoyo'))
            paredes.add(Pared(616 + (64 * 7) - 32, 60 + (64 * 7), 'hoyo'))
            paredes.add(Pared(616 + (64 * 7) - 32, 60 + (64 * 9), 'hoyo'))
            paredes.add(Pared(616 + (64 * 8) - 32, 60 + (64 * 7), 'hoyo'))

        if nivel == 4:
            #METAS
            meta1 = Meta(20 + (64 * 3) - 32, 60 + (64 * 5))

            meta2 = Meta(616 + (64 * 2) - 32, 60 + (64 * 1))

            #PAREDES
            paredes.empty()
            paredes.add(Pared(20 + (64 * 4) - 32, 60 + (64 * 5), 'piedra'))
            paredes.add(Pared(20 + (64 * 5) - 32, 60 + (64 * 4), 'piedra'))
            paredes.add(Pared(20 + (64 * 5) - 32, 60 + (64 * 6), 'piedra'))
            paredes.add(Pared(20 + (64 * 3) - 32, 60 + (64 * 7), 'piedra'))
            paredes.add(Pared(20 + (64 * 5) - 32, 60 + (64 * 1), 'piedra'))
            paredes.add(Pared(20 + (64 * 7) - 32, 60 + (64 * 2), 'piedra'))

            paredes.add(Pared(616 + (64 * 4) - 32, 60 + (64 * 5), 'hoyo'))
            paredes.add(Pared(616 + (64 * 6) - 32, 60 + (64 * 5), 'hoyo'))
            paredes.add(Pared(616 + (64 * 5) - 32, 60 + (64 * 6), 'hoyo'))
            paredes.add(Pared(616 + (64 * 9) - 32, 60 + (64 * 7), 'hoyo'))
            paredes.add(Pared(616 + (64 * 7) - 32, 60 + (64 * 7), 'hoyo'))
            paredes.add(Pared(616 + (64 * 1) - 32, 60 + (64 * 2), 'hoyo'))

            #PICOS
            picos.empty()
            picos.add(Picos(20 + (64 * 2) - 32, 60 + (64 * 5), 'enredadera', dalt))
            picos.add(Picos(20 + (64 * 1) - 32, 60 + (64 * 6), 'enredadera', dalt))

            picos.add(Picos(616 + (64 * 1) - 32, 60 + (64 * 1), 'rosales', dalt))
            picos.add(Picos(616 + (64 * 3) - 32, 60 + (64 * 2), 'rosales', dalt))

            #MOVILES
            movil1 = Movil(20 + (64 * 6) - 32, 60 + (64 * 5), 'escultura')
            movil2 = Movil(616 + (64 * 5) - 32, 60 + (64 * 4), 'estatua')
        
        if nivel == 5:
            WIN.blit(titulo_surface, (0,0))

    pygame.display.update()
    clock.tick(60)
    