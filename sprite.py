import pygame


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

    def draw(self, screen):
        screen.blit(self.image, self.rect)
