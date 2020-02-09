from enemy import Enemy
from sprites import *
from various import *
from functions import calculate_angle, calculate_distance
from enemy_gun import EnemyGun
from collider import Collider
from animator import Animator
from random import randint


class EnemySniper(Enemy):
    def __init__(self, player, x, y):
        super().__init__(player, x, y)
        self.range = 400
        self.speed_run = 50
        self.health = 3
        self.min_rapidity = 500
        self.max_rapidity = 2500
        self.damage_collide = 1
        self.weapon = EnemyGun(self)
        self.image = BULLETS["enemy_face"]
        self.images = {"left": BULLETS["enemy_left"], "right": BULLETS["enemy_right"], "up": BULLETS["enemy_back"],
                       "down": BULLETS["enemy_face"]}
        self.rect_f = list(self.image.get_rect().move(x, y))
        self.rect = pygame.Rect(self.rect_f)
        self.height_person = self.rect_f[H] * HEIGHT_UNIT_COLLIDER
        self.layer_collider = 2
        self.animation_duration = 0.3
        self.shot_count = 2
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
        self.animation_shot_back_1 = Animator(self, [BULLETS["enemy_back_shot_1"]] * 2, BULLETS["enemy_back"],
                                              self.animation_duration)
        self.animation_shot_back_2 = Animator(self, [BULLETS["enemy_back_shot_2"]] * 2, BULLETS["enemy_back"],
                                              self.animation_duration)
        self.animation_shot_left_1 = Animator(self, [BULLETS["enemy_left_shot_1"]] * 2, BULLETS["enemy_left"],
                                              self.animation_duration)
        self.animation_shot_left_2 = Animator(self, [BULLETS["enemy_left_shot_2"]] * 2, BULLETS["enemy_left"],
                                              self.animation_duration)
        self.animation_shot_right_1 = Animator(self, [BULLETS["enemy_right_shot_1"]] * 2, BULLETS["enemy_right"],
                                               self.animation_duration)
        self.animation_shot_right_2 = Animator(self, [BULLETS["enemy_right_shot_2"]] * 2, BULLETS["enemy_right"],
                                               self.animation_duration)
        self.animation_shot_face_1 = Animator(self, [BULLETS["enemy_face_shot_1"]] * 2, BULLETS["enemy_face"],
                                              self.animation_duration)
        self.animation_shot_face_2 = Animator(self, [BULLETS["enemy_face_shot_2"]] * 2, BULLETS["enemy_face"],
                                              self.animation_duration)
        self.active_animation = self.animation_shot_face_1

    def move(self):
        distance = calculate_distance(self.rect_f, self.player.rect_f)
        if distance > self.range:
            self.angle = calculate_angle(self.rect_f, self.player.rect_f)
            self.speed = self.speed_run
        else:
            self.speed = 0
        super().move()

    def attack(self):
        if not self.weapon.rapidity:
            shot = randint(1, self.shot_count)
            if shot == 1:
                if self.image == self.images["down"]:
                    self.change_animation(self.animation_shot_face_1)
                elif self.image == self.images["left"]:
                    self.change_animation(self.animation_shot_left_1)
                elif self.image == self.images["right"]:
                    self.change_animation(self.animation_shot_right_1)
                else:
                    self.change_animation(self.animation_shot_back_1)
            else:
                if self.image == self.images["down"]:
                    self.change_animation(self.animation_shot_face_2)
                elif self.image == self.images["left"]:
                    self.change_animation(self.animation_shot_left_2)
                elif self.image == self.images["right"]:
                    self.change_animation(self.animation_shot_right_2)
                else:
                    self.change_animation(self.animation_shot_back_2)
        super().attack()


