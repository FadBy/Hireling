from one_shoot_weapon import OneShootWeapon
from watchtimer import Timer


class Pistol(OneShootWeapon):
    def __init__(self, owner):
        super().__init__(owner)
        self.kill()
        self.time_rapidity = 0.7
        self.time_reload = 1
        self.damage = 1

        self.bandolier = 14
        self.ammo_in_magazine = 7
        self.full_ammo = 7

        self.timer_rapidity = Timer(self.time_rapidity, self.stop_timer_rapidity)






