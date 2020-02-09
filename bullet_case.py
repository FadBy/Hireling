from sprite import *
from sprites import *
from various import *
from collider import Collider
from consumable import Consumable


class BulletCase(Consumable):
    def __init__(self, player, x, y):
        super().__init__(player, x, y, ITEMS['bullet_case'])
        self.player = player
        self.load = 30
        self.rect_f[X] = x
        self.rect_f[Y] = y
        self.rect_f = list(self.image.get_rect().move(x, y))
        self.rect = pygame.Rect(self.rect_f)

    def unit_collided(self, collider, unit):
        if unit.owner.tag == "player":
            self.kill()
            for i in self.colliders:
                self.colliders[i].kill()
            super().changes('load', self.load)

    def move(self):
        pass
