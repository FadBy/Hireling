import pygame
from global_various import *


class Collider(pygame.sprite.Sprite):
    def __init__(self, owner, x, y, w, h):
        super().__init__()
        self.image = pygame.Surface((w, h))
        self.rect_f = [x + owner.rect_f[0], y + owner.rect_f[1], w, h]
        self.rect = pygame.Rect(*self.rect_f)
        self.owner = owner

    def change_pos(self, x, y):
        self.rect_f[0] -= x
        self.rect_f[1] -= y
        self.rect = pygame.Rect(self.rect_f)
