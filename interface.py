from various import *
from sprite import *
from sprites import *
from group import Group
import pygame


class Interface(Group):
    def __init__(self):
        super().__init__()
        interface_content.append(self)
        self.tag = "health"
        self.health = 5
        for i in range(self.health):
            sprite = Sprite(self)
            sprite.image = PLAYER["health_point"]
            sprite.rect_f = list(sprite.image.get_rect())
            sprite.rect_f[X], sprite.rect_f[Y] = (i + 1) * 75, 50
            sprite.rect = pygame.Rect(sprite.rect_f)

    def change_hp(self, hp):
        self.health = hp
        interface_content[0].empty()
        interface_content.clear()
        interface_content.append(self)
        for i in range(self.health):
            sprite = Sprite(self)
            sprite.image = PLAYER["health_point"]
            sprite.rect_f = list(sprite.image.get_rect())
            sprite.rect_f[X], sprite.rect_f[Y] = (i + 1) * 75, 50
            sprite.rect = pygame.Rect(sprite.rect_f)