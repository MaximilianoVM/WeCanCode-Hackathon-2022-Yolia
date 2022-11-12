import pygame

class Jugador(pygame.sprite.Sprite):
    def __init__(self, dalt, religion):
        super().__init__()

        self.religion = religion

        if self.religion == 'mexica':
            self.x = 308
            self.y = 380
        else:
            self.x = 904
            self.y = 380

        self.frames = []
        self.frame_index = 0

        #=================== CRISTIANO ===================#
        if self.religion == 'cristiano' :
            #=================== SIN DALTONISMO
            if dalt == False:
                jugador1 = pygame.transform.scale2x(pygame.image.load('assets/CalebCum/Sprite-0004.png').convert_alpha())
                jugador2 = pygame.transform.scale2x(pygame.image.load('assets/CalebCum/Sprite-0005.png').convert_alpha())
                jugador3 = pygame.transform.scale2x(pygame.image.load('assets/CalebCum/Sprite-0006.png').convert_alpha())
                jugador4 = pygame.transform.scale2x(pygame.image.load('assets/CalebCum/Sprite-0007.png').convert_alpha())
                jugador5 = pygame.transform.scale2x(pygame.image.load('assets/CalebCum/Sprite-0008.png').convert_alpha())
                jugador6 = pygame.transform.scale2x(pygame.image.load('assets/CalebCum/Sprite-0009.png').convert_alpha())
                jugador7 = pygame.transform.scale2x(pygame.image.load('assets/CalebCum/Sprite-0010.png').convert_alpha())
                jugador8 = pygame.transform.scale2x(pygame.image.load('assets/CalebCum/Sprite-0011.png').convert_alpha())

                self.jugadorWalk = [jugador1, jugador2, jugador3, jugador4, jugador5, jugador6, jugador7, jugador8]
            #=================== DALTONISMO
            else:
                print("dalt")
        
        #==================== MEXICA ====================#
        elif self.religion == 'mexica':
            #=================== SIN DALTONISMO
            if dalt == False:
                jugador1 = pygame.transform.scale2x(pygame.image.load('assets/CanekCum/fondoPrueba1.png').convert_alpha())
                jugador2 = pygame.transform.scale2x(pygame.image.load('assets/CanekCum/fondoPrueba2.png').convert_alpha())
                jugador3 = pygame.transform.scale2x(pygame.image.load('assets/CanekCum/fondoPrueba3.png').convert_alpha())
                jugador4 = pygame.transform.scale2x(pygame.image.load('assets/CanekCum/fondoPrueba4.png').convert_alpha())
                jugador5 = pygame.transform.scale2x(pygame.image.load('assets/CanekCum/fondoPrueba5.png').convert_alpha())
                jugador6 = pygame.transform.scale2x(pygame.image.load('assets/CanekCum/fondoPrueba6.png').convert_alpha())
                jugador7 = pygame.transform.scale2x(pygame.image.load('assets/CanekCum/fondoPrueba7.png').convert_alpha())
                jugador8 = pygame.transform.scale2x(pygame.image.load('assets/CanekCum/fondoPrueba8.png').convert_alpha())

                self.jugadorWalk = [jugador1, jugador2, jugador3, jugador4, jugador5, jugador6, jugador7, jugador8]
            #=================== DALTONISMO
            else:
                print("dalt")
        
        self.jugador_index = 0
        self.image = self.jugadorWalk[self.jugador_index]
        self.rect = self.image.get_rect(midbottom = (self.x, self.y))

    def animationState(self):
        self.jugador_index += 0.1
        if self.jugador_index >= len(self.jugadorWalk):
            self.jugador_index = 0
        self.image = self.jugadorWalk[int(self.jugador_index)]
    
    @staticmethod
    def playerInput(event, player1, player2):
        if event.key == pygame.K_DOWN:
            print('down')
            player1.sprite.rect.y += 64
            player2.sprite.rect.y += 64

        if event.key == pygame.K_UP:
            print('up')
            player1.sprite.rect.y -= 64
            player2.sprite.rect.y -= 64

        if event.key == pygame.K_LEFT:
            print('left')
            player1.sprite.rect.x -= 64
            player2.sprite.rect.x -= 64

        if event.key == pygame.K_RIGHT:
            print('right')
            player1.sprite.rect.x += 64
            player2.sprite.rect.x += 64

    def update(self):
        self.animationState()
    
    def collision_meta(self, meta):
        if self.rect.colliderect(meta.rect):
            return True
        else:
            return False

    def collision_picos(self, picos):
        if self.rect.colliderect(picos.rect):
            return True
        else:
            return False

    def restart(self):
        if self.religion == 'mexica':
            self.rect = self.image.get_rect(midbottom = (308, 380))
        else:
            self.rect = self.image.get_rect(midbottom = (904, 380))