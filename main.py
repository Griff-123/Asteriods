import pygame
from constants import *
from player import *

x = True
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
def main():
    x = True
    pygame.init
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    Player.containers = (updatable_group, drawable_group)
    user = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    fps = pygame.time.Clock()
    dt = 0
    print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    while x == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for user in drawable_group:
            user.draw(screen)
        pygame.display.flip()
        for user in updatable_group:
            user.update(dt)
        fps.tick(60)
        dt = fps.get_time() / 1000




if __name__ == "__main__":
    main()