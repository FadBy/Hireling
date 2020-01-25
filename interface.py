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
        self.bandolier = 10
        self.ammo_in_magazine = 31
        self.full_ammo = 30
        self.changes(self.health, self.ammo_in_magazine)

    def changes(self, hp, ammo):
        self.health = hp
        self.ammo_in_magazine = ammo
        if self.ammo_in_magazine <= 0:
            if self.bandolier >= 30:
                self.bandolier -= self.full_ammo
                self.ammo_in_magazine += 30
            elif self.bandolier < 30:
                self.ammo_in_magazine += self.bandolier
                self.bandolier = 0
        else:
            self.ammo_in_magazine -= 1
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
        if self.bandolier == 0 and self.ammo_in_magazine == 0:
            return 'empty'