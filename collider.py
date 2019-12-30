import pygame
from global_various import *


class Collider(pygame.sprite.Sprite):
    def __init__(self, owner, x, y, w, h):
        super().__init__()
        self.add(collider_group)
        self.image = pygame.Surface((w, h))
        self.rect_f = [x, y, w, h]
        self.rect = pygame.Rect(x, y, w, h)
        self.owner = owner

    def change_pos(self, x, y):
        self.rect_f[0] -= x
        self.rect_f[1] -= y
        self.rect = pygame.Rect(self.rect_f)
