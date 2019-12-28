from global_various import *


class Camera(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = [0] * 4

    def move_camera(self, x, y):
        self.rect[0] -= x
        self.rect[1] -= y

    def set_rect(self, rect):
        self.rect[2] = rect[2]
        self.rect[3] = rect[3]

    def set_pos(self, coords):
        self.rect[0] = coords[0]
        self.rect[1] = coords[1]
