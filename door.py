from camera import Camera
from all_various import *
from collider import Collider
from sprite import Sprite


class Door(Sprite):
    def __init__(self, owner, way, images, x, y):
        super().__init__(middle)
        self.owner = owner
        self.way = way
        self.open = False
        self.tag = "door"
        if way == "horisontal":
            self.image_close = images["door_close_hor"]
            self.image_open = images["door_open_hor"]
            self.image = self.image_close
            self.rect_f = list(self.image_close.get_rect())
            self.rect_f[X], self.rect_f[Y] = x + owner.rect_f[X], y + owner.rect_f[Y]
            self.rect = pygame.Rect(*self.rect_f)
            self.collider = Collider(self, 0, 0, self.rect_f[W], self.rect_f[H],
                                     trigger=True)
        else:
            self.image_close = images["door_close_ver"]
            self.image_open = images["door_open_ver"]
            self.image = self.image_close
            self.rect_f = list(self.image_close.get_rect())
            self.rect_f[X], self.rect_f[Y] = x + owner.rect_f[X], y + owner.rect_f[Y]
            self.rect = pygame.Rect(*self.rect_f)
            self.collider = Collider(self, 0, 0, self.rect_f[W], self.rect_f[H], trigger=True)

    def move_camera(self, x, y):
        self.rect_f[X] -= x
        self.rect_f[Y] -= y
        self.rect = pygame.Rect(self.rect_f)
        self.collider.move_camera(x, y)

    def draw(self, screen):
        super().draw(screen)
        self.image = self.image_close

    def unit_collided(self, unit):
        if unit.tag != "bullet":
            self.image = self.image_open


