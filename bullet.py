from collider import Collider
from various import *
from sprites import *
from functions import set_change_coord
from sprite import Sprite


class Bullet(Sprite):
    def __init__(self, owner, angle):
        super().__init__(middle, motionful)
        self.image = BULLETS["player_bullet"]
        self.angle = angle
        self.owner = owner
        self.rect_f = list(self.image.get_rect())
        self.set_pos()
        self.rect = pygame.Rect(*self.rect_f)
        self.speed = 300
        self.xspeed = None
        self.yspeed = None
        self.xspeed, self.yspeed = set_change_coord(angle, self.speed)
        self.colliders = []
        self.colliders.append(Collider(self, 0, 0, self.rect_f[W], self.rect_f[H], trigger=True))
        self.tag = "bullet"

    def set_pos(self):
        self.rect_f[X], self.rect_f[Y] = self.owner.rect_f[X] + self.owner.rect_f[W] // 2, self.owner.rect_f[Y] + \
                                         self.owner.rect_f[H] // 2
        if self.angle % 180 == 0:
            self.rect_f[Y] -= self.rect_f[H] // 2
        else:
            self.rect_f[X] -= self.rect_f[W] // 2

    def move(self):
        self.rect_f[X] += self.xspeed * self.tick
        self.rect_f[Y] += self.yspeed * self.tick
        self.rect = pygame.Rect(*self.rect_f)
        for i in self.colliders:
            i.move(self.xspeed * self.tick, self.yspeed * self.tick)

    def set_tick(self, tick):
        self.tick = tick

    def unit_collided(self, unit):
        if not (unit.owner.tag == self.owner.tag or (
                unit.owner in motionful and not unit.trigger) or unit.owner.tag == "bullet"):
            self.delete_from_all()

    def delete_from_all(self):
        self.kill()
        for i in self.colliders:
            i.kill()
