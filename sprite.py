from various import *


class Sprite(pygame.sprite.Sprite):
    def __init__(self, *args):
        self.lsts = []
        self.groups = []
        for i in args:
            if isinstance(i, pygame.sprite.Group):
                self.groups.append(i)
            else:
                self.lsts.append(i)
        super().__init__(self.groups)
        for i in self.lsts:
            i.append(self)
        self.image = None
        self.rect = None
        self.rect_f = None

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move_camera(self, x, y):
        self.rect_f[X] -= x
        self.rect_f[Y] -= y
        self.rect = pygame.Rect(self.rect_f)

    def kill(self):
        for i in self.lsts:
            if self in i:
                i.remove(self)
        super().kill()
