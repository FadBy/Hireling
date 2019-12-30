from camera import Camera
from global_various import *

class Door(Camera):
    def __init__(self, room, image, x, y):
        super().__init__()
        self.room = room
        self.image = load_image(image)
        self.rect_f = list(self.image.get_rect())
        self.rect_f[0], self.rect_f[1] = x, y
