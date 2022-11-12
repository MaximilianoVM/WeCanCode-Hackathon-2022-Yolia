import pygame

class Picos(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.x = x
        self.y = y

        self.frames = []
        self.frame_index = 0

        self.image = pygame.image.load('assets/Sprite-0006.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = (self.x, self.y))

    def collision(self, other):
         return self.rect.colliderect(other.rect)


