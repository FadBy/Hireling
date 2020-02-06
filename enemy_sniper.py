from enemy import Enemy
from sprites import *
from various import *
from functions import calculate_angle, calculate_distance
from enemy_gun import EnemyGun


class EnemySniper(Enemy):
    def __init__(self, player, x, y):
        super().__init__(player, x, y)
        self.range = 500
        self.speed_run = 50
        self.health = 5
        self.min_rapidity = 500
        self.max_rapidity = 2500
        self.damage_collide = 1
        self.weapon = EnemyGun(self)
        self.image = BULLETS["vorog"]
        self.rect_f = list(self.image.get_rect().move(x, y))
        self.rect = pygame.Rect(self.rect_f)

    def move(self):
        distance = calculate_distance(self.rect_f, self.player.rect_f)
        if distance > self.range:
            self.angle = calculate_angle(self.rect_f, self.player.rect_f)
            self.speed = self.speed_run
        else:
            self.speed = 0
        super().move()



