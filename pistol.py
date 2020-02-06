from weapon import Weapon
from sprites import ITEMS
import pygame
from bullet import Bullet
from collider import Collider


class Pistol(Weapon):
    def __init__(self, owner):
        super().__init__(owner)
        self.owner = owner
        self.time_rapidity = 0.3
        self.time_reload = 1
        self.damage = 1

        self.bandolier = 10
        self.ammo_in_magazine = 30
        self.full_ammo = 30

        self.owner.interface.changes(self.owner.health, self.ammo_in_magazine)

    def shoot(self, angle):
        Bullet(self.owner, angle)
        self.ammo_in_magazine -= 1
        self.owner.interface.changes(self.owner.health, self.ammo_in_magazine)





