import math
import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((900, 600))
clock = pygame.time.Clock()
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
    