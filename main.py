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
player1.add(Jugador(20+32+(4*64), 60+(5*64), False, 'mexica'))

player2 = pygame.sprite.GroupSingle()
player2.add(Jugador(WIDTH-20-32-(4*64), 60+(5*64), False, 'cristiano'))

fondo_surface = pygame.image.load('assets/HACKATHON FONDO TEMP.png').convert()


meta1 = Meta(52, 124)
meta2 = Meta(52 + 576 + 20, 124)

contador_fin = 0

while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            Jugador.playerInput(player1, event, player1, player2, WIDTH, HEIGHT)
            print(player2.sprite.rect.y)
            print(player2.sprite.rect.x)

    if game_active:
    
        WIN.blit(fondo_surface, (0,0))
        WIN.blit(meta1.image, meta1.rect)
        WIN.blit(meta2.image, meta2.rect)

        player1.draw(WIN)
        player1.update()
        
        player2.draw(WIN)
        player2.update()

        if (player1.sprite.collision_meta(meta1) and player2.sprite.collision_meta(meta2)):
            print(contador_fin)
            contador_fin += 1

            if contador_fin == 30:
                game_active = False

        player1.draw(WIN)
        player2.draw(WIN)

    else:
        WIN.blit(fondo_surface, (0,0))

    pygame.display.update()
    clock.tick(60)
