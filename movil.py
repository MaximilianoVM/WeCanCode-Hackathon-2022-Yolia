import pygame

class Movil(pygame.sprite.Sprite):
    def __init__(self, x, y,tipo):
        super().__init__()

        self.x = x
        self.y = y

        self.start_x = x
        self.start_y = y

        self.tipo = tipo

        if self.tipo=='estatua': #estatua es un obtaculo del cielo que reduce vida 
            self.image = pygame.image.load('assets/Estatuas/estatua.png').convert_alpha() # Carga imagen
            self.image = pygame.transform.scale2x(self.image) # Escala imagen a 2x

        elif self.tipo=='escultura': #escultura es obstaculo del mictlan que reduce vida 
            self.image = pygame.image.load('assets/Escultura/escultura.png').convert_alpha() # Carga imagen
            self.image = pygame.transform.scale2x(self.image) # Escala imagen a 2x

        self.rect = self.image.get_rect(midbottom = (self.x, self.y))
    
    def mover(self, pos_anterior):
        if pos_anterior[1] > self.rect.y:
            #ABAJO A ARRIBA
            print('======= IF UNO =======')
            print("pos anterior[1]: ", pos_anterior[1])
            print("pos actual y: ", self.rect.y)
            self.rect.y -= 64
            
        elif pos_anterior[1] < self.rect.y:
            #ARRIBA A ABAJO
            print('======= IF DOS =======')
            print("pos anterior[1]: ", pos_anterior[1])
            print("pos actual y: ", self.rect.y)
            self.rect.y += 64

        elif pos_anterior[0] > self.rect.x:
            #DERECHA A IZQUIERDA
            print('======= IF TRES =======')
            print("pos anterior[0]: ", pos_anterior[0])
            print("pos actual: x", self.rect.x)
            self.rect.x -= 64

        elif pos_anterior[0] < self.rect.x:
            #EMPUJA A LA DERECHA
            print('======= IF CUATRO =======')
            print("pos anterior[0]: ", pos_anterior[0])
            print("pos actualx: ", self.rect.x)
            self.rect.x += 64

        ############LIMITES############
        if self.tipo == 'escultura':
            if self.rect.x  > 532:
                self.rect.x = 532
            if self.rect.x  < 20:
                self.rect.x = 20
            if self.rect.y  > 572:
                self.rect.y = 572
            if self.rect.y  < 60:
                self.rect.y = 60

        if self.tipo == 'estatua':
            if self.rect.x  > 1128:
                self.rect.x = 1128
            if self.rect.x  < 616:
                self.rect.x = 616
            if self.rect.y  > 572:
                self.rect.y = 572
            if self.rect.y  < 60:
                self.rect.y = 60

    def collision_object(self, object):
        if self.rect.colliderect(object.rect):
            return True
        else:
            return False
    
    def reiniciar(self):
        self.rect = self.image.get_rect(midbottom = (self.start_x, self.start_y))