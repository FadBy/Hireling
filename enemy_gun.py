from weapon import Weapon
from watchtimer import Timer
from bullet import Bullet
from random import randint
from various import koef_dif
from sounds import *

class EnemyGun(Weapon):
    def __init__(self, owner):
        super().__init__(owner)
        self.kill()
        self.owner = owner
        self.rapidity = False
        if owner.player.difficult != 1:
            self.damage = 1 * (owner.player.difficult - 1) * koef_dif
        else:
            self.damage = 1
        self.max_rapidity = 2500
        self.min_rapidity = 1000

    def shoot(self, angle):
        if not self.rapidity:
            sniper_shot.play()
            Bullet(self.owner, angle)
            Timer(randint(self.min_rapidity, self.max_rapidity) / 1000, self.stop_timer_rapidity).start()
            self.rapidity = True
