from camera import Camera
from global_various import *
from collider import Collider


class Wall(Camera):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = load_image(image)
        self.rect_f = list(self.image.get_rect())
        self.rect_f[0], self.rect_f[1] = x, y
        self.rect = pygame.Rect(*self.rect_f)
        self.tag = "wall"

        if self.rect[2] > self.rect[3]:
            self.add(walls_hor_group)
            self.way = "horisontal"
            self.collider = Collider(self, wall_collider_group, x, y, self.rect[2],
                                     self.rect[3])
        else:
            walls_ver_group.add(self)
            self.way = "vertical"
            self.collider = Collider(self, wall_collider_group, x, y, self.rect[2],
                                     self.rect[3])

    def move_camera(self, x, y):
        super().move_camera(x, y)
        self.collider.change_pos(x, y)
