from camera import Camera
from global_various import *
from collider import Collider


class Wall(pygame.sprite.Group):
    def __init__(self, room, images, x, y, length, corners=None):
        super().__init__()
        self.thickness = room.thickness
        motionless.append(self)

        self.height_wall = room.height_wall
        self.length = length
        self.owner = room
        self.tag = "wall"
        if isinstance(images, list):
            self.way = "horisontal"
            walls.append(self)
            self.rect_f = [x + room.rect_f[0], y - self.height_wall + room.rect_f[1],
                           length * METR + self.thickness * 2,
                           self.height_wall + self.thickness]
            for i in range(len(corners)):
                corner = pygame.sprite.Sprite(self)
                if corners[i]:
                    corner.image = load_image(images[FULL_CORNER_SPRITE])
                else:
                    corner.image = load_image(images[NOT_FULL_CORNER_SPRITE])
                corner.rect = list(corner.image.get_rect())
                corner.rect[0], corner.rect[1] = self.rect_f[0] + i * length * METR + i * self.thickness, self.rect_f[1]
            for i in range(length):
                vertical = pygame.sprite.Sprite(self)
                vertical.image = pygame.transform.rotate(load_image(images[VERTICAL_SPRITE]), 90)
                vertical.rect = list(vertical.image.get_rect())
                vertical.rect[0], vertical.rect[1] = self.rect_f[0] + i * METR + self.thickness, self.rect_f[1]
            for i in range(length):
                wall_surface = pygame.sprite.Sprite(self)
                wall_surface.image = load_image(images[WALL_SPRITE])
                wall_surface.rect = list(wall_surface.image.get_rect())
                wall_surface.rect[0], wall_surface.rect[1] = self.rect_f[0] + i * METR + self.thickness, self.rect_f[
                    1] + self.thickness
            self.colliders = []
            self.colliders.append(Collider(self, 0, self.height_wall, self.rect_f[2], self.thickness))
        else:
            self.way = "vertical"
            walls.insert(0, self)
            self.rect_f = [x + room.rect_f[0], y - self.height_wall + self.thickness + room.rect_f[1], self.thickness,
                           length * METR]
            for i in range(length):
                wall_surface = pygame.sprite.Sprite(self)
                wall_surface.image = load_image(images)
                wall_surface.rect = list(wall_surface.image.get_rect())
                wall_surface.rect[0], wall_surface.rect[1] = self.rect_f[0], self.rect_f[1] + i * METR
            self.colliders = []
            self.colliders.append(Collider(self, 0, self.height_wall, self.rect_f[2], self.rect_f[3]))

    def move_camera(self, x, y):
        self.rect_f[0] -= x
        self.rect_f[1] -= y
        for i in self:
            i.rect[0] -= x
            i.rect[1] -= y
        for i in self.colliders:
            i.move_camera(x, y)

