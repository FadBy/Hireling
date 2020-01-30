from various import *
from sprites import *
from character import Character
from collider import Collider


class Enemy(Character):
    def __init__(self, player, x, y):
        super().__init__(middle, motionful, enemies)
        self.player = player
        self.tag = 'enemy'
        self.damage_collide = None
        self.damage_bullet = None
        self.image = BULLETS["vorog"]
        self.rect_f = list(self.image.get_rect())
        self.rect_f[X] = x
        self.rect_f[Y] = y
        self.rect = pygame.Rect(self.rect_f)
        self.height_person = self.rect_f[H] * HEIGHT_UNIT_COLLIDER
        self.colliders = {"default": Collider(self, WIDTH_UNIT_COLLIDER * self.rect_f[W], self.height_person,
                                              self.rect_f[W] - 2 * WIDTH_UNIT_COLLIDER * self.rect_f[W],
                                              self.rect_f[H] - self.height_person)}

    def unit_collided(self, collider, unit):
        pass

    def kill(self):
        super().kill()
        for i in self.colliders:
            self.colliders[i].kill()
