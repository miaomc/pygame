import pygame
from pygame.locals import *
from sys import exit
import math


pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

bg = (0,255,100)

plane = pygame.image.load('plane.png')
plane = pygame.transform.flip(plane,False,True)
position = (0, 0)

Fullscreen = False
clock = pygame.time.Clock()

# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

while True:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    if event.type == KEYDOWN:
        if event.key == K_f:
            Fullscreen = not Fullscreen
            if Fullscreen:
                screen = pygame.display.set_mode((1366, 768), FULLSCREEN, 32)
            else:
                screen = pygame.display.set_mode((640, 480), 0, 32)
        if event.key == K_a:
            position = position[0]-1, position[1]
        if event.key == K_d:
            position = position[0]+1, position[1]
        if event.key == K_w:
            position = position[0], position[1]-1
        if event.key == K_s:
            position = position[0], position[1]+1

           
    screen.fill(bg)
    screen.blit(plane, position)

    #pygame.draw.aaline(screen, [10,10,10], (1,1), (50,80))

    pygame.draw.line(screen, (255,0,0), (0,0),(100,200), 1)
    start_angle = math.radians(-45)
    end_angle = math.radians(100)
    pygame.draw.arc(screen, (0,0,0), (0,0,100,200), start_angle, end_angle, 1)
    #pygame.display.update()
    
    pygame.display.flip()
