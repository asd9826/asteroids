import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        centre = (self.x,self.y)
        pygame.draw.circle(screen,"white", centre,self.radius,2)

    def update(self, dt):
        