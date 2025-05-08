import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

card_surf = pygame.image.load("card_sprite_test.png")
rect = pygame.Rect(8, 759, 100, 50)
card_rect = card_surf.subsurface(rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill("black")
    screen.blit(card_rect, (100, 100))

    pygame.display.flip()
    clock.tick(60)