import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("R0B0 / K1LL")
clock = pygame.time.Clock()
test_font = pygame.font.Font('fonts/RobotRoc.otf', 32)

game_active = False
start_time = 0
