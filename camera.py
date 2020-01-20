from all_various import *


class Camera:
    def __init__(self):
        super().__init__()
        self.rect_f = None
        self.rect = None
        self.image = None

    def move_camera(self, x, y):
        self.rect_f[X] -= x
        self.rect_f[Y] -= y
        self.rect = pygame.Rect(self.rect_f)

