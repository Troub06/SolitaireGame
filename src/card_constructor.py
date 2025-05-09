from configs import *

import pygame
from sys import exit

class Card:
    def __init__(self, card_name: str):
        self.card_name = card_name

class Constructor:
    def __init__(self):
        self.card_surf = pygame.image.load("../assets/card_sprite.png")
        # self.card_surf = pygame.image.load(CARD_SPRITE_URL)

    def construct(self):
        cards = {}
        for symbol in SYMBOLS:
            for number in NUMBERS:
                card = Card(symbol + number)
                card
                cards[symbol + number] = card

# pygame.init()
# screen = pygame.display.set_mode((800, 600))
# clock = pygame.time.Clock()

# card_surf = pygame.image.load("../assets/card_sprite_test.png")
# rect = pygame.Rect(923, 2, 172, 236)
# card_rect = card_surf.subsurface(rect)

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()

#     screen.fill("black")
#     screen.blit(card_rect, (100, 100))

#     pygame.display.flip()
#     clock.tick(60)