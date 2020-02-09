from sprites import ITEMS
from watchtimer import Timer
from collider import Collider
from various import *
from one_shoot_weapon import OneShootWeapon


class Automat(OneShootWeapon):
    def __init__(self, owner, x, y):
        super().__init__(owner)
        self.time_rapidity = 0.1
        if GOD:
            self.time_reload = 0.1
            self.damage = 999
        else:
            self.time_reload = 3
            self.damage = 1
        self.image = ITEMS["machine_gun"]
        self.rect_f = self.image.get_rect().move(x - self.image.get_rect()[X] // 2, y - self.image.get_rect()[Y] // 2)
        self.rect = pygame.Rect(self.rect_f)

        self.bandolier = 30
        self.ammo_in_magazine = 30
        self.full_ammo = 30

        self.colliders = {"default": Collider(self, 0, 0, self.rect_f[W], self.rect_f[H], True)}

        self.timer_rapidity = Timer(self.time_rapidity, self.stop_timer_rapidity)
