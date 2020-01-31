from various import *
from sprites import *
from character import Character
from collider import Collider
from functions import set_change_coord


class Enemy(Character):
    def __init__(self, player, x, y):
        super().__init__(middle, motionful, enemies)
        self.player = player
        self.tag = 'enemy'
        self.angle = 0
        self.damage_collide = None
        self.damage_bullet = None
        self.speed = None
        self.image = BULLETS["vorog"]
        self.rect_f = list(self.image.get_rect())
        self.rect_f[X] = x
        self.rect_f[Y] = y
        self.rect = pygame.Rect(self.rect_f)
        self.height_person = self.rect_f[H] * HEIGHT_UNIT_COLLIDER
        self.colliders = {"default": Collider(self, WIDTH_UNIT_COLLIDER * self.rect_f[W], self.height_person,
                                              self.rect_f[W] - 2 * WIDTH_UNIT_COLLIDER * self.rect_f[W],
                                              self.rect_f[H] - self.height_person),
                          "bullet_hit": Collider(self, INDENT_UNIT_COLLIDET * self.rect_f[W],
                                                 INDENT_UNIT_COLLIDET * self.rect_f[H],
                                                 self.rect_f[W] - 2 * INDENT_UNIT_COLLIDET * self.rect_f[W],
                                                 self.rect_f[H] - INDENT_UNIT_COLLIDET * self.rect_f[H], True),
                          "collide_with_enemy": Collider(self, WIDTH_UNIT_COLLIDER * self.rect_f[W],
                                                         self.height_person,
                                                         self.rect_f[W] - WIDTH_UNIT_COLLIDER * 2 * self.rect_f[W],
                                                         self.rect_f[H] - self.height_person, True)
                          }

    def move(self):
        coord = set_change_coord(self.angle, self.speed)
        self.rect_f[X] += coord[X] * self.tick
        self.rect_f[Y] += coord[Y] * self.tick
        for i in self.colliders:
            self.colliders[i].move(coord[X] * self.tick, coord[Y] * self.tick)

    def unit_collided(self, collider, unit):
        pass

    def kill(self):
        super().kill()
        for i in self.colliders:
            self.colliders[i].kill()

