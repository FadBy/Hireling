from camera import Camera
from global_various import *


class Surface(Camera):
    def __init__(self, x, y):
        super().__init__()
        self.add_in_lst(self)
        self.set_pos((x, y))
        self.image = load_image("background.png", -1)
        self.set_rect(self.image.get_rect())
