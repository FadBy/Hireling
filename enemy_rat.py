from enemy import Enemy
from sprites import BULLETS
from enemy_shotgun import EnemyShotgun
import pygame
from functions import calculate_angle, calculate_distance

class EnemyRat(Enemy):
    def __init__(self, player, x, y):
        super().__init__(player, x, y)
        self.range = 300
        self.speed_run = 200
        self.speed_escape = 300
        self.health = 5
        self.min_rapidity = 3000
        self.max_rapidity = 3000
        self.damage_collide = 1
        self.weapon = EnemyShotgun(self)
        self.image = BULLETS["vorog_rat"]
        self.rect_f = list(self.image.get_rect().move(x, y))
        self.rect = pygame.Rect(self.rect_f)
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
