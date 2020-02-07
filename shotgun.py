from weapon import Weapon
from sprites import ITEMS
from watchtimer import Timer
from bullet import Bullet
from collider import Collider
from various import *
from random import randint


class Shotgun(Weapon):
    def __init__(self, owner, x, y):
        super().__init__(owner)
        self.owner = owner
        self.time_rapidity = 0.5
        self.tag = "weapon"
        self.time_reload = 2
        self.damage = 0.5
        self.image = ITEMS["shotgun"]
        self.rect_f = self.image.get_rect().move(x, y)
        self.rect = pygame.Rect(self.rect_f)

        self.bandolier = 10
        self.ammo_in_magazine = 5
        self.full_ammo = 5
        self.count_bullets = 6
        self.angle_dispertion = 60
        self.distance_bullet = 500

        self.colliders = {"default": Collider(self, 0, 0, self.rect_f[W], self.rect_f[H], True)}

        self.rapidity = False

        self.timer_rapidity = Timer(self.time_rapidity, self.stop_timer_rapidity)

    def stop_timer_rapidity(self):
        self.rapidity = False

    def shoot(self, angle):
        if not self.rapidity and not self.reload_process:
            if self.ammo_in_magazine != 0:
                self.ammo_in_magazine -= 1
                self.rapidity = True
                self.timer_rapidity.start()
                for i in range(self.count_bullets):
                    bullet = Bullet(self.owner, angle + randint(-self.angle_dispertion // 2,
                                                                self.angle_dispertion // 2), self.distance_bullet)
                self.owner.interface.set_ammo()

