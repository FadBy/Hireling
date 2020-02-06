from various import *
from sprites import *
from collider import Collider
from sprite import Sprite


class Consumable(Sprite):
    def __init__(self, player, x, y, image):
        super().__init__(middle, motionful)
        self.player = player
        self.tag = 'consumable'
        self.image = image
        self.tick = None
        self.rect_f = list(self.image.get_rect())
        self.rect_f[X] = x
        self.rect_f[Y] = y
        self.rect = pygame.Rect(self.rect_f)
        self.height_person = self.rect_f[H] * WIDTH_UNIT_COLLIDER
        self.colliders = {"default": Collider(self, 0, self.height_person, self.rect_f[W],
                                 self.rect_f[H] - self.height_person, True)}

    def changes(self, type, quantity):
        if type == 'heal':
            self.player.heal(quantity)
        elif type == 'load':
            self.player.load(quantity)

    def set_tick(self, tick):
        self.tick = tick

