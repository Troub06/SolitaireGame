from src.configs import *

import pygame

class Card:
    def __init__(self, card_name: str):
        self.card_name = card_name.split()
        if self.card_name[0] == "heart" or self.card_name[0] == "diamond":
            self.color = "red"
        else:
            self.color = "black"
        self.card_sprite = pygame.image.load(CARD_SPRITE_URL).convert_alpha()

    def construct(self):
        self.surf = pygame.Surface(CARD_SIZE)
        pygame.draw.rect(self.surf, "white", CARD_SIZE_RECT, border_radius=15)
        
        if 74 <= ord(self.card_name[1][0]) <= 81: # работаем с персонажем
            # рисует персонажа
            rect = pygame.Rect(COORDINATES[f"{self.color}{self.card_name[1]}"])
            element_surf = self.card_sprite.subsurface(rect)
            element_rect = element_surf.get_rect(midbottom = (CARD_SIZE[0] // 2, CARD_SIZE[1]))
            self.surf.blit(element_surf, element_rect)
            # рисует маленькую цифру
            rect = pygame.Rect(COORDINATES[f"{self.color}{self.card_name[1]} letter"])
            element_surf = self.card_sprite.subsurface(rect)
            element_rect = element_surf.get_rect(center = (35, 40))
            self.surf.blit(element_surf, element_rect)
            # рисует маленькую масть
            rect = pygame.Rect(COORDINATES[f"{self.card_name[0]} mini"])
            element_surf = self.card_sprite.subsurface(rect)
            element_rect = element_surf.get_rect(center = (131, 40))
            self.surf.blit(element_surf, element_rect)
        else: # работаем с цифрой
            # рисует большую масть
            rect = pygame.Rect(COORDINATES[f"{self.card_name[0]}"])
            element_surf = self.card_sprite.subsurface(rect)
            element_rect = element_surf.get_rect(midbottom = (CARD_SIZE[0] // 2, CARD_SIZE[1]-2))
            self.surf.blit(element_surf, element_rect)
            # рисует маленькую цифру
            rect = pygame.Rect(COORDINATES[f"{self.color}{self.card_name[1]}"])
            element_surf = self.card_sprite.subsurface(rect)
            element_rect = element_surf.get_rect(center = (35, 40))
            self.surf.blit(element_surf, element_rect)
            # рисует маленькую масть
            rect = pygame.Rect(COORDINATES[f"{self.card_name[0]} mini"])
            element_surf = self.card_sprite.subsurface(rect)
            element_rect = element_surf.get_rect(center = (131, 40))
            self.surf.blit(element_surf, element_rect)

class Constructor:
    def __init__(self):
        self.card_surf = pygame.image.load(CARD_SPRITE_URL)

    def construct(self):
        self.cards = {} # словарь поверхностей
        for symbol in SYMBOLS:
            for number in NUMBERS:
                card = Card(symbol + " " + number)
                card.construct()
                self.cards[symbol + number] = card.surf
