from weapon import Weapon
from collider import Collider
from various import *
from watchtimer import Timer


class Melle(Weapon):
    def __init__(self, owner):
        super().__init__(owner)
        self.time_attack = 0.7
        self.rapidity = False
        self.damage = 3
        self.shootable = False
        self.collider = Collider(self.owner, self.owner.rect_f[W] * 0.3, -0.15 * self.owner.rect_f[H],
                                 self.owner.rect_f[W] * 0.4, self.owner.rect_f[H] * 0.4, True)
        self.timer = Timer(self.time_attack, self.stop_timer_rapidity)
        self.kill()

    def stop_timer_rapidity(self):
        self.rapidity = False

    def shoot(self, angle):
        if not self.rapidity:
            colliders = pygame.sprite.spritecollide(self.collider, enemies, False)
            for i in colliders:
                if pygame.sprite.collide_rect(self.collider, i.colliders["collide_with_enemy"]):
                    i.hit_from_enemy(self.damage)
            self.timer.start()
            self.rapidity = True
            self.owner.animation_attack_melee_up.start()

