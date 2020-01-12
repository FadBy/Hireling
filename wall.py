from all_various import *
from collider import Collider
from door import Door


class Wall(pygame.sprite.Group):
    def __init__(self, owner, way, images, x, y, length, coord_of_doors, corners=None):
        super().__init__()
        self.way = way
        self.thickness = owner.thickness
        motionless.append(self)
        self.height_wall = owner.height_wall
        self.length = length
        self.owner = owner
        self.tag = "wall"
        self.colliders = []
        self.doors = []
        coord_of_doors2 = []
        for i in coord_of_doors:
            for j in i[1:]:
                coord_of_doors2.append(j)
        coord_of_doors = coord_of_doors2
        if way == "horisontal":
            walls.append(self)
            self.rect_f = [x + owner.rect_f[0], y - self.height_wall + owner.rect_f[1],
                           length * METR + self.thickness * 2,
                           self.height_wall + self.thickness]
            for i in range(len(corners)):
                corner = pygame.sprite.Sprite(self)
                if corners[i]:
                    corner.image = images["full_corner"]
                else:
                    corner.image = images["not_full_corner"]
                corner.rect = list(corner.image.get_rect())
                corner.rect[0], corner.rect[1] = self.rect_f[0] + i * length * METR + i * self.thickness, self.rect_f[1]
            for i in range(length):
                vertical = pygame.sprite.Sprite(self)
                vertical.image = pygame.transform.rotate(images["wall_block_ver"], 90)
                vertical.rect = list(vertical.image.get_rect())
                vertical.rect[0], vertical.rect[1] = self.rect_f[0] + i * METR + self.thickness, self.rect_f[1]
                if i + 1 in coord_of_doors:
                    self.doors.append(Door(self, "horisontal", images, i * METR + self.thickness, 0))
                else:
                    wall_surface = pygame.sprite.Sprite(self)
                    wall_surface.image = images["wall_block_hor"]
                    wall_surface.rect = list(wall_surface.image.get_rect())
                    wall_surface.rect[0], wall_surface.rect[1] = self.rect_f[0] + i * METR + self.thickness, self.rect_f[
                        1] + self.thickness
                    self.colliders.append(
                        Collider(self, i * METR + self.thickness, self.height_wall, METR, self.thickness))
            self.colliders.append(Collider(self, 0, self.height_wall, self.thickness, self.thickness))
            self.colliders.append(Collider(self, self.rect_f[2] - self.thickness, self.height_wall, self.thickness, self.thickness))

        else:
            walls.insert(0, self)
            self.rect_f = [x + owner.rect_f[0], y - self.height_wall + self.thickness +owner.rect_f[1], self.thickness,
                           length * METR]
            for i in range(length):
                if i + 1 == coord_of_doors:
                    self.doors.append(Door(self, "vertical", images, self.rect_f[0] + i * METR + self.thickness, self.rect_f[1]))
                wall_surface = pygame.sprite.Sprite(self)
                wall_surface.image = images["wall_block_ver"]
                wall_surface.rect = list(wall_surface.image.get_rect())
                wall_surface.rect[0], wall_surface.rect[1] = self.rect_f[0], self.rect_f[1] + i * METR
                self.colliders.append(Collider(self, 0, self.height_wall + METR * i, self.rect_f[2], METR))


    def move_camera(self, x, y):
        self.rect_f[0] -= x
        self.rect_f[1] -= y
        for i in self:
            i.rect[0] -= x
            i.rect[1] -= y
        for i in self.doors:
            i.move_camera(x, y)
        for i in self.colliders:
            i.move_camera(x, y)

    def draw(self, screen):
        super().draw(screen)
        for i in self.doors:
            i.draw(screen)



