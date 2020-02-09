from door import Door
from sprite import Sprite
from group import Group
from collider import Collider
from various import *


class Wall(Group):
    def __init__(self, owner, way, images, x, y, length, coord_of_doors):
        super().__init__()
        decors.append(self)
        self.way = way
        self.height = owner.height
        self.width = owner.width
        self.length = length
        self.owner = owner
        self.tag = "wall"
        self.colliders = []
        self.doors = []
        self.layer_collider = 3
        coord_of_doors2 = []
        for i in coord_of_doors:
            for j in i[1:]:
                coord_of_doors2.append(j)
        coord_of_doors = coord_of_doors2
        if way == "up" or way == "down":
            self.rect_f = [x + owner.rect_f[X], y + owner.rect_f[Y],
                           length * METR + self.width * 2,
                           self.height]
            if way == "up":
                corner_image = images["corner_up"]
            else:
                corner_image = images["corner_down"]
            for i in range(2):
                corner = Sprite(self, middle, decors)
                if i == 0:
                    corner.image = corner_image
                else:
                    corner.image = pygame.transform.flip(corner_image, True, False)
                corner.rect_f = list(corner.image.get_rect())
                corner.rect_f[X] = self.rect_f[X] + i * (self.rect_f[W] - corner.rect_f[W])
                corner.rect_f[Y] = self.rect_f[Y]
            for i in range(length):
                if i + 1 in coord_of_doors:
                    self.doors.append(Door(self, "horisontal", images, i * METR + self.width, 0))
                elif i not in coord_of_doors:
                    wall_surface = Sprite(self, middle, decors)
                    wall_surface.image = images["wall_block_hor"]
                    wall_surface.rect_f = list(wall_surface.image.get_rect())
                    wall_surface.rect_f[X] = self.rect_f[X] + i * METR + self.width
                    wall_surface.rect_f[Y] = self.rect_f[Y]
                    self.colliders.append(
                        Collider(self, i * METR + self.width, self.height - METR, METR,
                                 METR))

            if way == "up":
                self.colliders.append(Collider(self, 0, self.height - METR, self.width,
                                               METR))
                self.colliders.append(
                    Collider(self, self.rect_f[2] - self.width, self.height - METR, self.width,
                             METR))
            else:
                self.colliders.append(Collider(self, 0, 0, self.width, self.height))
                self.colliders.append(
                    Collider(self, self.rect_f[W] - self.width, 0, self.width, self.height))

        else:
            self.rect_f = [x + owner.rect_f[X], y + owner.rect_f[Y], self.width,
                           length * METR]
            for i in range(length):
                if i + 1 in coord_of_doors:
                    self.doors.append(Door(self, "vertical", images, 0, i * METR))
                elif i not in coord_of_doors:
                    wall_surface = Sprite(self, middle, decors)
                    wall_surface.image = images["wall_block_ver"]
                    wall_surface.rect_f = list(wall_surface.image.get_rect())
                    wall_surface.rect_f[X], wall_surface.rect_f[Y] = self.rect_f[X], self.rect_f[Y] + i * METR
                    self.colliders.append(Collider(self, 0, METR * i, self.rect_f[W], METR))
