from weapon import Weapon
from watchtimer import Timer
from bullet import Bullet


class OneShootWeapon(Weapon):
    def __init__(self, owner):
        super().__init__(owner)
        self.owner = owner
        self.time_rapidity = 0
        self.tag = "weapon"
        self.time_reload = 0
        self.damage = 0

        self.bandolier = 0
        self.ammo_in_magazine = 0
        self.full_ammo = 0

        self.rapidity = False

        self.timer_rapidity = Timer(self.time_rapidity, self.stop_timer_rapidity)

    def shoot(self, angle):
        if not self.rapidity and not self.reload_process:
            if self.ammo_in_magazine != 0:
                self.ammo_in_magazine -= 1
                self.rapidity = True
                self.timer_rapidity.start()
                Bullet(self.owner, angle)
                self.owner.interface.set_ammo()
