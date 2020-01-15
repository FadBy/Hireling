from all_various import *
from sprite import Sprite


class Surface(pygame.sprite.Group):
    def __init__(self, room, images, x, y, w, h):
        super().__init__()
        background.append(self)
        self.owner = room
        self.tag = "surface"
        self.rect_f = [x + room.rect_f[0], y + room.rect_f[1], w * METR, h * METR]

        for i in range(w):
            for j in range(h):
                sprite = Sprite(self)
                sprite.image = images["surface_block"]
                sprite.rect = list(sprite.image.get_rect())
                sprite.rect[0], sprite.rect[1] = self.rect_f[0] + i * METR, self.rect_f[1] + j * METR

    def move_camera(self, x, y):
        self.rect_f[0] -= x
        self.rect_f[1] -= y
        for i in self:
            i.rect[0] -= x
            i.rect[1] -= y







