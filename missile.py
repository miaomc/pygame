import pygame
import os, sys

BACKGROUND_COLOR = (50, 10, 255)
WHITE = (255, 255, 255)
FPS = 60

class Missile(pygame.sprite.Sprite):
    def __init__(self, position, direction,fuel):
        pygame.sprite.Sprite.__init__(self)
        self.position = position
        self.direction = direction
        self.fuel = fuel


class HomingMissile(Missile):
    def __init__(self, position, direction, velocity_value=3.53553, accelerate_value=0.02828, max_fuel=150):
        Missile.__init__(self, position=position, direction=position, fuel=max_fuel)
##        self.velocity=  velocity
##        self.accelerate = accelerate
        self.velocity = [1, 1]
        self.accelerate = [0.02, -0.02]
        
        self.image = pygame.image.load('homingmissile.png').convert()
        self.image.set_colorkey(WHITE)
        self.position = position
        self.rect = self.image.get_rect(center=position)
        
    def update(self):
        for i in [0,1]:
            self.velocity[i] += self.accelerate[i]
            self.position[i] += self.velocity[i]
        self.rect.center = self.position
        self.fuel -= 1
        if self.fuel < 0:
            self.remove()

    def remove(self):
        self.kill()
        
    
class Control():
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.done = False
        self.fps = FPS
        self.clock = pygame.time.Clock()
        self.groups = pygame.sprite.Group()
        self.groups.add(HomingMissile([10,400],(1,0)))

    def event_loop(self):
        for event in pygame.event.get():
            self.keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT or self.keys[pygame.K_ESCAPE]:
                self.done = True

    def update(self):
        self.groups.update()#self.screen_rect)
        
    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.groups.draw(self.screen)
        
    def main_loop(self):
        while not self.done:
            self.event_loop()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(self.fps)
            
if __name__ == "__main__":
    SCREEN_SIZE = (600, 600)

    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    
    pygame.display.set_mode(SCREEN_SIZE)

    run_it = Control()
    run_it.main_loop()
    pygame.quit()
    sys.exit()
