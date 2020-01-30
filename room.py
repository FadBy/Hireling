from wall import Wall
from surface import Surface
from various import *
from collider import Collider


class Room:
    def __init__(self, player, images, x, y, w, h, doors, arena=False):
        rooms.append(self)
        self.arena = arena
        self.player = player
        self.doors = []
        self.height = images["wall_block_hor"].get_rect()[H]
        self.width = images["wall_block_ver"].get_rect()[W]
        self.rect_f = [x, y, w * METR + self.width * 2, h * METR + self.height * 2]
        self.tag = "room"
        self.walls = {"up": [], "down": [], "left": [], "right": []}
        self.spawn_area = [3 * METR + self.rect_f[X], 3 * METR + self.rect_f[Y], self.rect_f[W] - 6 * METR,
                           self.rect_f[H] - 6 * METR]
        self.colliders = {
            "default": Collider(self, 3 * METR, 3 * METR, self.rect_f[W] - 6 * METR, self.rect_f[H] - 6 * METR, True),
            "check_door": Collider(self, METR, METR, self.rect_f[W] - 2 * METR, self.rect_f[H] - 2 * METR, True)}
        for i in range(len(doors)):
            self.walls[doors[i][0]].append(doors[i])
        for i in self.walls:
            if i == "up":
                self.walls[i] = Wall(self, "up", images, 0, 0, w, self.walls[i])
            elif i == "down":
                self.walls[i] = Wall(self, "down", images, 0, self.rect_f[H] - self.height, w,
                                     self.walls[i])
            elif i == "left":
                self.walls[i] = Wall(self, "vertical", images, 0, self.height, h, self.walls[i])
            else:
                self.walls[i] = Wall(self, "vertical", images, self.rect_f[W] - self.width, self.height, h,
                                     self.walls[i])
        self.surface = Surface(self, images, self.width, self.height, w, h)

    def move_camera(self, x, y):
        self.rect_f[X] -= x
        self.rect_f[Y] -= y
        self.surface.move_camera(x, y)
        for i in self.walls:
            self.walls[i].move_camera(x, y)

    def draw(self, screen):
        self.surface.draw(screen)
        for i in self.walls:
            self.walls[i].draw(screen)

    def unit_collided(self, collider, unit):
        pass

    def collide_rect(self, unit):
        if (unit.rect_f[X] < self.rect_f[X] + self.rect_f[W] and unit.rect_f[X] > self.rect_f[X] or unit.rect_f[X] +
            unit.rect_f[W] > self.rect_f[X] and unit.rect_f[X] + unit.rect_f[W] < self.rect_f[X] + self.rect_f[W]) \
                and (
                unit.rect_f[Y] < self.rect_f[Y] + self.rect_f[H] and unit.rect_f[Y] > self.rect_f[Y] or unit.rect_f[Y] +
                unit.rect_f[H] > self.rect_f[Y] and unit.rect_f[Y] + unit.rect_f[H] < self.rect_f[Y] + self.rect_f[H]):
            return True
        else:
            return False
