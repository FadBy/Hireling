from camera import Camera
from all_various import *
from collider import Collider
from sprite import Sprite


class Door(Sprite):
    def __init__(self, owner, way, images, x, y):
        super().__init__(motionless, middle)
        self.owner = owner
        self.way = way
        self.open = False
        if way == "horisontal":
            self.image_close = images["door_close_hor"]
            self.image_open = images["door_open_hor"]
            self.image = self.image_close
            self.rect_f = list(self.image_close.get_rect())
            self.rect_f[0], self.rect_f[1] = x + owner.rect_f[0], y + owner.rect_f[1]
            self.rect = pygame.Rect(*self.rect_f)
            self.collider = Collider(self, 0, 0, self.rect_f[2], self.rect_f[3],
                                     trigger=True)
        else:
            self.image_close = images["door_close_ver"]
            self.image_open = images["door_open_ver"]
            self.image = self.image_close
            self.rect_f = list(self.image_close.get_rect())
            self.rect_f[0], self.rect_f[1] = x + owner.rect_f[0], y + owner.rect_f[1]
            self.rect = pygame.Rect(*self.rect_f)
            self.collider = Collider(self, 0, 0, self.rect_f[2], self.rect_f[3], trigger=True)

    def move_camera(self, x, y):
        self.rect_f[0] -= x
        self.rect_f[1] -= y
        self.rect = pygame.Rect(self.rect_f)
        self.collider.move_camera(x, y)

    def draw(self, screen):
        super().draw(screen)
        self.image = self.image_close


    def unit_collided(self):
        self.image = self.image_open


