from various import *
from sprites import *


class Group(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.rect_f = None

    def move_camera(self, x, y):
        self.rect_f[X] -= x
        self.rect_f[Y] -= y
        for i in self:
            i.move_camera(x, y)
