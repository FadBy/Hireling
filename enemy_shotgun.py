from weapon import Weapon
from watchtimer import Timer
from bullet import Bullet
from random import randint
from various import koef_dif

class EnemyShotgun(Weapon):
    def __init__(self, owner):
        super().__init__(owner)
        self.kill()
        self.owner = owner
        self.rapidity = False
        if owner.player.difficult != 1:
            self.damage = 0.5 * (owner.player.difficult - 1) * koef_dif
        else:
            self.damage = 0.5
        self.time_rapidity = 2
        self.count_bullets = 4
        self.distance_bullet = 500
        self.angle_dispertion = 60

    def shoot(self, angle):
        for i in range(self.count_bullets):
            Bullet(self.owner, angle + randint(-self.angle_dispertion // 2,
                                                        self.angle_dispertion // 2), self.distance_bullet)
        Timer(self.time_rapidity, self.stop_timer_rapidity).start()
        self.rapidity = True
