from sprite import Sprite
from various import *


class Weapon(Sprite):
    def __init__(self, owner):
        super().__init__(middle, object_sprites)
        self.owner = owner
        self.image = None
        self.time_rapidity = 0
        self.time_reload = 0
        self.damage = 0
        self.colliders = None

        self.rapidity = False

        self.bandolier = 0
        self.ammo_in_magazine = 0
        self.full_ammo = 0

    def unit_collided(self, collider, unit):
        if unit.owner.tag == "player":
            self.kill()
            self.rect_f = self.owner.rect_f.copy()
            self.colliders["default"].kill()
            self.owner.weapon = self
            self.owner.interface.set_ammo()


    def stop_timer_rapidity(self):
        self.rapidity = False
