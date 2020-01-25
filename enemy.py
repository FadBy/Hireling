from various import *
from sprites import *
from character import Character
from collider import Collider
from map import player


class Enemy(Character):
    def __init__(self, x, y):
        super().__init__(middle, motionful, enemies)
        self.enemy_hp = 100
        self.tag = 'enemy'
        self.damage_collide = None
        self.damage_bullet = None
        self.image = BULLETS["vorog"]
        self.rect_f = list(self.image.get_rect())
        self.rect_f[X] = x
        self.rect_f[Y] = y
        self.rect = pygame.Rect(self.rect_f)
        self.height_person = self.rect_f[H] * HEIGHT_UNIT_COLLIDER
        self.colliders.append(Collider(self, WIDTH_UNIT_COLLIDER, self.height_person,
                                       self.rect_f[W] - 2 * WIDTH_UNIT_COLLIDER,
                                       self.rect_f[H] - self.height_person))
        self.colliders.append(
            Collider(self, INDENT_UNIT_COLLIDET * self.rect_f[W], INDENT_UNIT_COLLIDET * self.rect_f[H],
                     self.rect_f[W] - 2 * INDENT_UNIT_COLLIDET * self.rect_f[W],
                     self.rect_f[H] - 2 * INDENT_UNIT_COLLIDET * self.rect_f[H], True))

    def unit_collided(self, unit):
        if unit.owner.tag == "player":
            player.hit_from_enemy(self.damage_collide)
