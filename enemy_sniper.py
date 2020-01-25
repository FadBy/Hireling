from enemy import Enemy
from bullet import Bullet
from math import atan, pi
from watchtimer import Timer
from random import randint
from sprites import *
from various import *
from map import player


class EnemySniper(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.min_rapidity = 500
        self.max_rapidity = 2500
        self.image = BULLETS["vorog"]
        self.rect_f = list(self.image.get_rect().move(x, y))
        self.rect = pygame.Rect(self.rect_f)
        self.rapidity = False

    def attack(self):
        if not self.rapidity:
            playerx = player.rect_f[X] + player.rect_f[W] // 2
            playery = player.rect_f[Y] + player.rect_f[H] // 2
            enemyx = self.rect_f[X] + self.rect_f[W] // 2
            enemyy = self.rect_f[Y] + self.rect_f[H] // 2
            angle = atan(abs(playerx - enemyx) / abs(playery - enemyy)) * 180 / pi
            if playerx > enemyx and playery < enemyy:
                angle = 90 - angle
            elif playerx < enemyx and playery < enemyy:
                angle = 90 + angle
            elif playerx < enemyx and playery > enemyy:
                angle = 270 - angle
            else:
                angle = 270 + angle
            bullet = Bullet(self, angle)
            print(randint(self.min_rapidity, self.max_rapidity) / 1000)
            Timer(randint(self.min_rapidity, self.max_rapidity) / 1000, self.stop_timer_rapidity).start()
            self.rapidity = True

    def move(self):
        pass

