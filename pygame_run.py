import pygame
import sys
pygame.init()

size = width, height = 352, 288
speed = [-1,1]
bg = (255,255,255)

screen = pygame.display.set_mode(size)

pygame.display.set_caption('FirstMove')

plane = pygame.image.load('plane.png')
plane = pygame.transform.flip(plane,False,True)
position = plane.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    position = position.move(speed)

    if position.left < 0 or position.right > width:
        plane = pygame.transform.flip(plane,True,False)
        speed[0] = -speed[0]

    if position.top < 0 or position.bottom > height:
        plane = pygame.transform.flip(plane,False,True)
        speed[1] = -speed[1]

    screen.fill(bg)
    screen.blit(plane,position)
    pygame.display.flip()

    pygame.time.delay(10)
