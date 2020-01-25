from various import *
from sprites import *
from character import Character
from collider import Collider
from map import player


class Enemy(Character):
    def __init__(self, x, y):
        super().__init__(middle, motionful, enemies)
        self.damage = 1
        self.enemy_hp = 100
        self.tag = 'enemy'
        self.image = BULLETS["vorog"]
        self.rect_f = list(self.image.get_rect())
        self.rect_f[X] = x
        self.rect_f[Y] = y
        self.rect = pygame.Rect(self.rect_f)
        self.height_person = self.rect_f[H] * WIDTH_UNIT_COLLIDER
        self.collider = Collider(self, 0, self.height_person, self.rect_f[W],
                                 self.rect_f[H] - self.height_person, True)

    def unit_collided(self, unit):
        if unit.tag != "bullet":
            player.hit_from_enemy(self.damage)
