from sprite import *
from sprites import *
from various import *
from collider import Collider
from consumable import Consumable


class Aid(Consumable):
    def __init__(self, player, x, y):
        super().__init__(player, x, y, ITEMS['aid'])
        self.heal = 1
        self.rect_f[X] = x
        self.rect_f[Y] = y
        self.rect_f = list(self.image.get_rect().move(x, y))
        self.rect = pygame.Rect(self.rect_f)

    def unit_collided(self, collider, unit):
        if unit.owner.tag == "player" and unit == unit.owner.colliders["bullet_hit"]:
            super().changes('heal', self.heal)
            self.kill()
            for i in self.colliders:
                self.colliders[i].kill()

    def move(self):
        pass
