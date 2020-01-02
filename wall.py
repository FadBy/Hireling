from camera import Camera
from global_various import *
from collider import Collider


class Wall(pygame.sprite.Group):
    def __init__(self, room, images, x, y, length, corners=None):
        self.thickness = room.thickness
        motionless.append(self)
        self.height_wall = room.height_wall
        self.length = length
        super().__init__()
        self.owner = room
        self.tag = "wall"
        if isinstance(images, list):
            self.way = "horisontal"
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
            self.collider = Collider(self, 0, self.height_wall, self.rect_f[2], self.thickness)
            collider_group.add(self.collider)
        else:
            self.way = "vertical"
            self.rect_f = [x + room.rect_f[0], y - self.height_wall + self.thickness + room.rect_f[1], self.thickness,
                           length * METR]
            for i in range(length):
                wall_surface = pygame.sprite.Sprite(self)
                wall_surface.image = load_image(images)
                wall_surface.rect = list(wall_surface.image.get_rect())
                wall_surface.rect[0], wall_surface.rect[1] = self.rect_f[0], self.rect_f[1] + i * METR
            self.collider = Collider(self, 0, self.height_wall, self.thickness, self.length * METR)
            collider_group.add(self.collider)

    def player_collided(self, player):
        self.collider.default_collide(player)

    def move_camera(self, x, y):
        self.rect_f[0] -= x
        self.rect_f[1] -= y
        for i in self:
            i.rect[0] -= x
            i.rect[1] -= y
