import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import sys
from shot import *


def main():
    pygame.init
    fps = pygame.time.Clock()
    screens = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()
   
    Asteroid.containers = (asteroids_group, updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group)
    
    asteroid_field = AsteroidField()
    Shot.containers = (updatable_group, drawable_group, shot_group)
    Player.containers = (updatable_group, drawable_group)
    user = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    dt = 0
    
    print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
       
        for obj in updatable_group:
            obj.update(dt)
        
        for obj in asteroids_group:
            if obj.collision(user) == True:
                print("Game Over")
                pygame.quit()
                sys.exit()
            

        screens.fill((0,0,0))
        
        for obj in drawable_group:
            obj.draw(screens)
        
        pygame.display.flip()
        
        dt = fps.tick(60) / 1000




if __name__ == "__main__":
    main()