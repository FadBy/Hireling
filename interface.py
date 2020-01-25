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
        self.bandolier = 70
        self.ammo_in_magazine = 30
        self.full_ammo = 30
        self.change_hp(self.health)

    def change_hp(self, hp):
        self.health = hp
        interface_content[0].empty()
        interface_content.clear()
        interface_content.append(self)
        for i in range(self.health):
            sprite = Sprite(self)
            sprite.image = PLAYER["health_point"]
            sprite.rect_f = list(sprite.image.get_rect())
            sprite.rect_f[X], sprite.rect_f[Y] = 20 + i * 75, 30
            sprite.rect = pygame.Rect(sprite.rect_f)
        dividing_line = Sprite(self)
        dividing_line.image = PLAYER["dividing_line"]
        dividing_line.rect_f = list(dividing_line.image.get_rect())
        dividing_line.rect_f[X], dividing_line.rect_f[Y] = width - 90, height - 150
        dividing_line.rect = pygame.Rect(dividing_line.rect_f)
        for i in range(len(str(self.ammo_in_magazine))):
            number = Sprite(self)
            number.image = PLAYER[str(self.ammo_in_magazine)[i]]
            number.rect_f = list(dividing_line.image.get_rect())
            number.rect_f[X], number.rect_f[Y] = width - 85 + i * 20, height - 130
            number.rect = pygame.Rect(number.rect_f)
        for i in range(len(str(self.bandolier))):
            number = Sprite(self)
            number.image = PLAYER[str(self.bandolier)[i]]
            number.rect_f = list(dividing_line.image.get_rect())
            number.rect_f[X], number.rect_f[Y] = width - 85 + i * 20, height - 60
            number.rect = pygame.Rect(number.rect_f)
