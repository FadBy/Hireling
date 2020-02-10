from weapon import Weapon
from collider import Collider
from various import *
from watchtimer import Timer
from sprites import ITEMS
from sounds import *


class Melle(Weapon):
    def __init__(self, owner):
        super().__init__(owner)
        self.time_attack = 0.7
        self.rapidity = False
        if not GOD:
            self.damage = 2
        else:
            self.damage = 999
        self.shootable = False
        self.image = ITEMS["pickaxe"]
        self.rect_f = [0] * 4
        self.rect = pygame.Rect(self.rect_f)
        self.radius_ver = 200
        self.radius_hor = 50
        self.collider = Collider(self.owner, -self.radius_hor, -self.radius_ver,
                                 self.owner.rect_f[W] + self.radius_hor * 2,
                                 self.owner.rect_f[H] + self.radius_ver * 1.5, True)
        self.timer = Timer(self.time_attack, self.stop_timer_rapidity)
        self.kill()

    def stop_timer_rapidity(self):
        self.rapidity = False

    def shoot(self, angle):
        if not self.rapidity:
            punch.play()
            thrill.play()
            colliders = pygame.sprite.spritecollide(self.collider, enemies, False)
            for i in colliders:
                if pygame.sprite.collide_rect(self.collider, i.colliders["collide_with_enemy"]):
                    i.hit_from_enemy(self.damage)
            self.timer.start()
            self.rapidity = True
            self.owner.animation_attack_melee_up.start()
            self.owner.active_animation = self.owner.animation_attack_melee_up
