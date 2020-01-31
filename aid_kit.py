from sprite import *
from sprites import *
from various import *
from collider import Collider
from consumable import Consumable


class Aid(Consumable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.heal = 1
        self.rect_f[X] = x
        self.rect_f[Y] = y
        self.rect_f = list(self.image.get_rect().move(x, y))
        self.rect = pygame.Rect(self.rect_f)

    def unit_collided(self, collider, unit):
        if unit.owner.tag == "player":
            super().changes('heal', self.heal)

    def move(self):
        pass
