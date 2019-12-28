from camera import Camera
from global_various import *
from collider import Collider


class Wall(Camera):
    def __init__(self, image, x, y, thickness, height):
        super().__init__()
        self.image = load_image(image)
        self.set_rect(self.image.get_rect())
        self.set_pos((x, y))
        if self.rect[2] > self.rect[3]:
            walls_hor_group.add(self)
            self.way = "horisontal"
        else:
            walls_ver_group.add(self)
            self.way = "vertical"








