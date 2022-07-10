# non OOP Version

import math
from random import randint

import pygame
from sys import exit

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_X = 900
SCREEN_Y = 600

PLAYER_PADDLE_POS_X = 10
PLAYER_PADDLE_SIZE_X = 10
player_paddle_size_y = 100
player_paddle_speed = 10

ENEMY_PADDLE_POS_X = SCREEN_X - 10
ENEMY_PADDLE_SIZE_X = 10
enemy_paddle_size_y = 50
enemy_paddle_speed = 10

ball_speed = 5
ball_size_x = 10
ball_size_y = 10

pygame.init()

screen = pygame.display.set_mode((900, 600))
clock = pygame.time.Clock()
pygame.display.update()
pygame.display.set_caption("Pong")

player_paddle_surface = pygame.Surface([PLAYER_PADDLE_SIZE_X, player_paddle_size_y])
player_paddle_surface.fill(WHITE)
player_paddle_rect = player_paddle_surface.get_rect(center=(PLAYER_PADDLE_POS_X, SCREEN_Y / 2))

enemy_paddle_surface = pygame.Surface([ENEMY_PADDLE_SIZE_X, enemy_paddle_size_y])
enemy_paddle_surface.fill(WHITE)
enemy_paddle_rect = player_paddle_surface.get_rect(center=(ENEMY_PADDLE_POS_X, SCREEN_Y / 2))

ball_surface = pygame.Surface([ball_size_x, ball_size_y])
ball_surface.fill(WHITE)
ball_rect = ball_surface.get_rect(center=(SCREEN_X / 2, SCREEN_Y / 2))
ball_velocity = [ball_speed, randint(-ball_speed, ball_speed)]

clock = pygame.time.Clock()


def bounce(ball):
    pass


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
    
    if ball_rect.centery < enemy_paddle_rect.centery:
        enemy_paddle_rect.centery -= min(player_paddle_speed, enemy_paddle_rect.centery - ball_rect.centery)
    elif ball_rect.centery > enemy_paddle_rect.centery:
        enemy_paddle_rect.centery += min(player_paddle_speed, ball_rect.centery - enemy_paddle_rect.centery)
    
    if ball_rect.top <= 0 or ball_rect.bottom >= SCREEN_Y:
        ball_velocity[1] *= -1
    elif ball_rect.colliderect(player_paddle_rect) or ball_rect.colliderect(enemy_paddle_rect):
        ball_velocity[0] *= -1
        ball_velocity[1] = randint(-ball_speed, ball_speed)
        
    ball_rect.centerx += ball_velocity[0]
    ball_rect.centery += ball_velocity[1]
    
    screen.blit(player_paddle_surface, player_paddle_rect)
    screen.blit(enemy_paddle_surface, enemy_paddle_rect)
    screen.blit(ball_surface, ball_rect)
    
    pygame.draw.line(screen, WHITE, [SCREEN_X / 2, 0], [SCREEN_X / 2, SCREEN_Y], 5)
    
    pygame.display.flip()
    clock.tick(60)
