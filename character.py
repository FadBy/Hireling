from sprite import *
from various import *
from sprites import *
from functions import *


class Character(Sprite):
    def __init__(self, *args):
        super().__init__(*args)
        self.timers = {}
        self.rect_f = []
        self.rect = []
        self.speed_run = None
        self.health = None
        self.full_health = None
        self.angle = None

    def set_tick(self, tick):
        self.tick = tick

    def move(self, speed):
        coord = set_change_coord(self.angle, speed)
        self.rect_f[X] += coord[X] * self.tick
        self.rect_f[Y] += coord[Y] * self.tick
        self.rect = pygame.Rect(self.rect_f)


