import pygame
from constants import *
x = True

def main():
    x = True
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    while x == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.fill((0,0,0))
        pygame.display.flip()





if __name__ == "__main__":
    main()