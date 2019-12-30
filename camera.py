from global_various import *


class Camera(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect_f = None
        self.rect = None
        self.image = None

    def move_camera(self, x, y):
        self.rect_f[0] -= x
        self.rect_f[1] -= y
        self.rect = pygame.Rect(self.rect_f)

