import pygame

pygame.init()

BLACK = (0,0,0)
size = width, height = (1000, 800)
bg = (50, 10, 255)
fps = 10

p1 = (10, 10)
p2 = (500, 360)

pygame.display.set_caption('Two Points')

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

vx, vy = 20, 20
acc = (1, -1)
done = False
x,y = p1
track = []

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
        
    vx += acc[0]
    vy += acc[1]
    x += vx
    y += vy
    track.append((x,y))
    screen.fill(bg)
    for i in track:
        pygame.draw.circle(screen, BLACK, (i[0],i[1]), 4)
    pygame.draw.circle(screen, BLACK, p2, 4)
    pygame.draw.line(screen, BLACK, p1, (p1[0]+1000, p1[1]+1000), 4)
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
