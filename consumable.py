from various import *
from sprites import *
from character import Character
from collider import Collider
from map import player
from sprite import Sprite


class Consumable(Sprite):
    def __init__(self, x, y):
        super().__init__(middle, motionful)
        self.tag = 'consumable'
        self.image = ITEMS["aid"]
        self.tick = None
        self.rect_f = list(self.image.get_rect())
        self.rect_f[X] = x
        self.rect_f[Y] = y
        self.rect = pygame.Rect(self.rect_f)
        self.height_person = self.rect_f[H] * WIDTH_UNIT_COLLIDER
        self.colliders = {"default": Collider(self, 0, self.height_person, self.rect_f[W],
                                 self.rect_f[H] - self.height_person, True)}

    def changes(self, type, quantity):
        if type == 'heal':
            player.heal(quantity)
        elif type == 'load':
            player.load(quantity)

    def set_tick(self, tick):
        self.tick = tick

