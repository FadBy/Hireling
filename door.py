from camera import Camera
from all_various import *
from collider import Collider


class Door(pygame.sprite.Sprite):
    def __init__(self, owner, way, images, x, y):
        super().__init__()
        motionless.append(self)
        self.owner = owner
        self.way = way

        if way == "horisontal":
            self.image = images["door_close"]
            self.rect_f = list(self.image.get_rect())
            self.rect_f[0], self.rect_f[1] = x + owner.rect_f[0], y + owner.rect_f[1]
            self.rect = pygame.Rect(*self.rect_f)
            self.collider = Collider(self, 0, owner.height_wall, self.rect_f[2], self.rect_f[3] - owner.height_wall,
                                     trigger=True)
        else:
            self.image = images["door_open"]
            self.rect_f = list(self.image.get_rect())
            self.rect_f[0], self.rect_f[1] = x + owner.rect_f[0], y + owner.rect_f[1]
            self.rect = pygame.Rect(*self.rect_f)
            self.collider = Collider(self, 0, 0, self.rect_f[2], self.rect_f[3])

    def move_camera(self, x, y):
        self.rect_f[0] -= x
        self.rect_f[1] -= y
        self.rect = pygame.Rect(self.rect_f)
        self.collider.move_camera(x, y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)








