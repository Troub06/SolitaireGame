from src.configs import *

import pygame
from sys import exit

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # render the game

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()