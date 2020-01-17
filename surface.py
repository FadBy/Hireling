from all_various import *
from sprite import Sprite


class Surface(pygame.sprite.Group):
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
                sprite.rect = list(sprite.image.get_rect())
                sprite.rect[X], sprite.rect[Y] = self.rect_f[X] + i * METR, self.rect_f[Y] + j * METR

    def move_camera(self, x, y):
        self.rect_f[X] -= x
        self.rect_f[Y] -= y
        for i in self:
            i.rect[X] -= x
            i.rect[Y] -= y







