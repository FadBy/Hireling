from enemy import Enemy
from sprites import BULLETS
from enemy_shotgun import EnemyShotgun
from functions import calculate_angle, calculate_distance
from various import *
from collider import Collider

class EnemyRat(Enemy):
    def __init__(self, player, x, y):
        super().__init__(player, x, y)
        self.range = 300
        self.speed_run = 100
        self.speed_escape = 150
        self.health = 2
        self.min_rapidity = 3000
        self.max_rapidity = 3000
        self.damage_collide = 1
        self.weapon = EnemyShotgun(self)
        self.image = BULLETS["enemy_2_face"]
        self.rect_f = list(self.image.get_rect().move(x, y))
        self.rect = pygame.Rect(self.rect_f)
        self.height_person = self.rect_f[H] * HEIGHT_UNIT_COLLIDER
        self.layer_collider = 2
        self.images = {"left": BULLETS["enemy_2_left"], "right": BULLETS["enemy_2_right"], "up": BULLETS["enemy_2_back"],
                       "down": BULLETS["enemy_2_face"]}
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
        self.escape = False

    def attack(self):
        distance = calculate_distance(self.rect_f, self.player.rect_f)
        if not self.weapon.rapidity and self.escape:
            self.escape = False
        if distance <= self.range and not self.escape:
            super().attack()
            self.escape = True

    def move(self):
        distance = calculate_distance(self.rect_f, self.player.rect_f)
        if self.escape:
            self.angle = (calculate_angle(self.rect_f, self.player.rect_f) + 180) % 360
            self.speed = self.speed_escape
        elif distance > self.range:
            self.angle = calculate_angle(self.rect_f, self.player.rect_f)
            self.speed = self.speed_run
        else:
            self.escape = True
        super().move()
