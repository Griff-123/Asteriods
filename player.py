import pygame
from circleshape import *
from constants import *
from main import screen



class Player(CircleShape):
    def __init__(self, x, y):
        self.radius = PLAYER_RADIUS
        rotation = 0
        self.rotation = rotation
        super().__init__(x, y, self.radius)
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self,screen):
        pygame.draw.polygon(screen, (255,255,255), Player.triangle(self), 2 )