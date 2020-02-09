from sprite import Sprite
from various import *
from watchtimer import Timer
from sounds import *

class Weapon(Sprite):
    def __init__(self, owner):
        super().__init__(middle, object_sprites)
        self.owner = owner
        self.image = None
        self.time_rapidity = 0
        self.time_reload = 0
        self.damage = 0
        self.colliders = None

        self.reload_process = False
        self.rapidity = False
        self.shootable = True

        self.bandolier = 0
        self.ammo_in_magazine = 0
        self.full_ammo = 0

    def unit_collided(self, collider, unit):
        if unit.owner.tag == "player":
            self.kill()
            self.rect_f = self.owner.rect_f.copy()
            self.colliders["default"].kill()
            self.owner.weapons.append(self)
            self.owner.weapon = self
            self.owner.interface.set_ammo()

    def load_bullets(self):
        self.bandolier += self.full_ammo

    def stop_timer_rapidity(self):
        self.rapidity = False

    def stop_timer_reload(self):
        if self.bandolier + self.ammo_in_magazine >= self.full_ammo:
            self.bandolier -= self.full_ammo - self.ammo_in_magazine
            self.ammo_in_magazine += self.full_ammo - self.ammo_in_magazine
        else:
            self.ammo_in_magazine = self.bandolier + self.ammo_in_magazine
            self.bandolier = 0
        self.owner.interface.set_ammo()
        self.reload_process = False

    def reload(self):
        if self.ammo_in_magazine != self.full_ammo and self.bandolier != 0 and not self.reload_process:
            reload.play()
            Timer(self.time_reload, self.stop_timer_reload).start()
            self.reload_process = True
