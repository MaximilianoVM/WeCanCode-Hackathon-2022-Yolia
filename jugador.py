import pygame

class Jugador(pygame.sprite.Sprite):
    def __init__(self, x, y, dalt):
        super().__init__()

        self.x = x
        self.y = y

        self.frames = []
        self.frame_index = 0

        self.image = pygame.image.load('assets/Sprite-0006.png').convert_alpha() # Cambiar Sprite
        self.rect = self.image.get_rect(midbottom = (self.x, self.y))

        if dalt == False:
            jugador_blue_1 = pygame.transform.scale2x(pygame.image.load('assets/Caleb/Caleb1.png').convert_alpha())
            jugador_blue_2 = pygame.transform.scale2x(pygame.image.load('assets/Caleb/Caleb2.png').convert_alpha())
            jugador_blue_3 = pygame.transform.scale2x(pygame.image.load('assets/Caleb/Caleb3.png').convert_alpha())
            jugador_blue_4 = pygame.transform.scale2x(pygame.image.load('assets/Caleb/Caleb4.png').convert_alpha())
            jugador_blue_5 = pygame.transform.scale2x(pygame.image.load('assets/Caleb/Caleb5.png').convert_alpha())
            jugador_blue_6 = pygame.transform.scale2x(pygame.image.load('assets/Caleb/Caleb6.png').convert_alpha())
            jugador_blue_7 = pygame.transform.scale2x(pygame.image.load('assets/Caleb/Caleb7.png').convert_alpha())
            jugador_blue_8 = pygame.transform.scale2x(pygame.image.load('assets/Caleb/Caleb8.png').convert_alpha())

            self.jugadorWalk = [jugador_blue_1, jugador_blue_2, jugador_blue_3, jugador_blue_4, jugador_blue_5, jugador_blue_6, jugador_blue_7, jugador_blue_8]
        else:
            print("dalt")
        
        self.jugador_index = 0
        self.image = self.jugadorWalk[self.jugador_index]
        self.rect = self.image.get_rect(midbottom = (self.x, self.y))

    def playerInput(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= 5
            self.jugador_index += 1
            if self.jugador_index >= len(self.jugadorWalk):
                self.jugador_index = 0
            self.image = self.jugadorWalk[self.jugador_index]

        if keys[pygame.K_RIGHT] and self.rect.x < 1212:
            self.rect.x += 5
            self.jugador_index += 1
            if self.jugador_index >= len(self.jugadorWalk):
                self.jugador_index = 0
            self.image = self.jugadorWalk[self.jugador_index]

        if keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= 5
            self.jugador_index += 1
            if self.jugador_index >= len(self.jugadorWalk):
                self.jugador_index = 0
            self.image = self.jugadorWalk[self.jugador_index]
            
        if keys[pygame.K_DOWN] and self.rect.y < 656:
            self.rect.y += 5
            self.jugador_index += 1
            if self.jugador_index >= len(self.jugadorWalk):
                self.jugador_index = 0
            self.image = self.jugadorWalk[self.jugador_index]
