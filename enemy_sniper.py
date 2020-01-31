from enemy import Enemy
from bullet import Bullet
from math import atan, pi
from watchtimer import Timer
from random import randint
from sprites import *
from various import *
from functions import calculate_angle, calculate_distance


class EnemySniper(Enemy):
    def __init__(self, player, x, y):
        super().__init__(player, x, y)
        self.range = 200
        self.speed_run = 200
        self.health = 5
        self.min_rapidity = 500
        self.max_rapidity = 2500
        self.damage_collide = 1
        self.damage_bullet = 1
        self.image = BULLETS["vorog"]
        self.rect_f = list(self.image.get_rect().move(x, y))
        self.rect = pygame.Rect(self.rect_f)
        self.rapidity = False

    def move(self):
        self.run()
        super().move()

    def attack(self):
        if not self.rapidity:
            angle = calculate_angle(self.rect_f, self.player.rect_f)
            bullet = Bullet(self, angle)
            Timer(randint(self.min_rapidity, self.max_rapidity) / 1000, self.stop_timer_rapidity).start()
            self.rapidity = True

    def run(self):
        distance = calculate_distance(self.rect_f, self.player.rect_f)
        if distance > self.range:
            self.angle = calculate_angle(self.rect_f, self.player.rect_f)
            self.speed = self.speed_run



