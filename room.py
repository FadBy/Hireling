from camera import Camera
from global_various import *
from wall import Wall


class Room(Camera):
    def __init__(self, image, x, y, thickness=1, height=1):
        super().__init__()
        surface_group.add(self)
        self.set_pos((x, y))
        self.image = load_image(image)
        self.set_rect(self.image.get_rect())
        Wall(image, x, y, thickness, height)








