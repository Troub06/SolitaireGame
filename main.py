from src.configs import *

import pygame
from sys import exit


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # создать поверхность -> нарисовать на ней элементы -> создать rect -> screen.blit
    surf = pygame.Surface(CARD_SIZE)
    surf.fill("white")
    element_surf = pygame.image.load(CARD_SPRITE_URL).convert_alpha()
    rect = pygame.Rect(COORDINATES["Red king"])
    element_surf = element_surf.subsurface(rect)
    element_rect = element_surf.get_rect(midbottom = (171 // 2, 236))
    surf.blit(element_surf, element_rect)
    rect = surf.get_rect(center = (400, 300))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # render the game
        screen.blit(surf, rect)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
