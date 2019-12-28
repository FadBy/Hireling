import pygame


class Collider:
    def __init__(self, owner, group, x, y, w, h, triger=False):
        self.surface = pygame.sprite.Sprite(group)
        self.image = pygame.Surface(w, h)
        self.rect = pygame.Rect(x, y, w, h)
        self.owner = owner




