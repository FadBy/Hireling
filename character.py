from sprite import Sprite
from various import *
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
        self.tick = None
        self.rapidity = False

    def set_tick(self, tick):
        self.tick = tick

    def stop_timer_rapidity(self):
        self.rapidity = False

