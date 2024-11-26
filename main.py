import pygame
from constants import *
x = True

def main():
    x = True
    pygame.init
    fps = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    while x == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.fill((0,0,0))
        pygame.display.flip()
        fps.tick(60)
        dt = fps.get_time() / 1000





if __name__ == "__main__":
    main()