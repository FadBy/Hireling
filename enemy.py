from all_various import *
from sprite import Sprite
from collider import *
from player import Player

class Enemy(Sprite):
    def __init__(self, enemy_type, x, y):
        super().__init__(middle, object_sprites)
        self.damage = 1
        self.enemy_hp = 100
        self.enemy_type = enemy_type
        self.tag  = 'enemy'
        self.image = BULLETS[self.enemy_type]
        self.rect_f = list(self.image.get_rect())
        self.rect_f[X] = x
        self.rect_f[Y] = y
        self.rect = pygame.Rect(self.rect_f)
        self.height_person = self.rect_f[H] * WIDTH_UNIT_COLLIDER
        self.collider = Collider(self, 0, self.height_person, self.rect_f[W],
                                 self.rect_f[H] - self.height_person, True)
        self.attack = 0

    def unit_collided(self, unit):
        if unit.tag != "bullet":
            self.attack = -1

