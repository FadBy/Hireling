from sprite import Sprite
from group import Group
from various import *


class Surface(Group):
    def __init__(self, room, images, x, y, w, h):
        super().__init__()
        background.append(self)
        self.owner = room
        self.tag = "surface"
        self.rect_f = [x + room.rect_f[X], y + room.rect_f[Y], w * METR, h * METR]
        for i in range(w):
            for j in range(h):
                sprite = Sprite(self)
                sprite.image = images["surface_block"]
                sprite.rect_f = list(sprite.image.get_rect())
                sprite.rect_f[X], sprite.rect_f[Y] = self.rect_f[X] + i * METR, self.rect_f[Y] + j * METR
