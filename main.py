# non OOP Version

import math
import pygame
from sys import exit

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_X = 900
SCREEN_Y = 600
PLAYER_PADDLE_POS_X = 10
PLAYER_PADDLE_SIZE_X = 10
player_paddle_size_y = 50
player_paddle_speed = 10

pygame.init()

screen = pygame.display.set_mode((900, 600))
clock = pygame.time.Clock()
pygame.display.update()
pygame.display.set_caption("Pong")

player_paddle_surface = pygame.Surface([PLAYER_PADDLE_SIZE_X, player_paddle_size_y])
player_paddle_surface.fill(WHITE)
player_paddle_rect = player_paddle_surface.get_rect(center=(PLAYER_PADDLE_POS_X, SCREEN_Y / 2))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
    screen.fill(BLACK)
    mouse_pos = pygame.mouse.get_pos()
    
    if mouse_pos[1] < player_paddle_rect.centery:
        player_paddle_rect.centery -= min(player_paddle_speed, player_paddle_rect.centery - mouse_pos[1])
    elif mouse_pos[1] > player_paddle_rect.centery:
        player_paddle_rect.centery += min(player_paddle_speed, mouse_pos[1] - player_paddle_rect.centery)
    
    screen.blit(player_paddle_surface, player_paddle_rect)
    pygame.draw.line(screen, WHITE, [SCREEN_X / 2, 0], [SCREEN_X / 2, SCREEN_Y], 5)

    pygame.display.flip()
    clock.tick(60)
    