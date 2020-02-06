from sprite import Sprite
from various import *
from functions import *
from collider import Collider


class Character(Sprite):
    def __init__(self, *args):
        super().__init__(*args)
        self.colliders = []
        self.timers = {}
        self.rect_f = []
        self.rect = []
        self.speed_run = None
        self.health = None
        self.full_health = None
        self.angle = None
        self.tick = None
        self.rapidity = False
        self.colliders = {}
        self.past_motion_x = 0
        self.past_motion_y = 0

    def hit_from_enemy(self, hp):
        self.health -= hp

    def set_tick(self, tick):
        self.tick = tick

    def stop_timer_rapidity(self):
        self.rapidity = False

