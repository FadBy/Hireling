from weapon import Weapon
from sprites import ITEMS
import pygame
from watchtimer import Timer
from bullet import Bullet
from collider import Collider
from various import *


class Automat(Weapon):
    def __init__(self, owner, x, y):
        super().__init__(owner)
        self.owner = owner
        self.time_rapidity = 0.1
        self.tag = "weapon"
        self.time_reload = 1
        self.damage = 1
        self.image = ITEMS["pistol"]
        self.rect_f = self.image.get_rect().move(x, y)
        self.rect = pygame.Rect(self.rect_f)

        self.bandolier = 10
        self.ammo_in_magazine = 30
        self.full_ammo = 30

        self.colliders = {"default": Collider(self, 0, 0, self.rect_f[W], self.rect_f[H], True)}

        self.rapidity = False

        self.timer_rapidity = Timer(self.time_rapidity, self.stop_timer_rapidity)

    def stop_timer_rapidity(self):
        self.rapidity = False

    def unit_collided(self, collider, unit):
        if unit.owner.tag == "player":
            self.kill()
            self.rect_f = self.owner.rect_f.copy()
            self.colliders["default"].kill()
            self.owner.weapon = self
            self.owner.interface.set_ammo()

    def shoot(self, angle):
        if not self.rapidity:
            if self.ammo_in_magazine != 0:
                self.ammo_in_magazine -= 1
                self.rapidity = True
                self.timer_rapidity.start()
                bullet = Bullet(self.owner, angle)
                self.owner.interface.set_ammo()
