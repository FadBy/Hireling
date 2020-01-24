from wall import *
from surface import *
from various import *


class Room:
    def __init__(self, images, x, y, w, h, doors):
        rooms.append(self)
        self.height = images["wall_block_hor"].get_rect()[H]
        self.width = images["wall_block_ver"].get_rect()[W]
        self.rect_f = [x, y, w * METR + self.width * 2, h * METR + self.height * 2]
        self.tag = "room"
        self.walls = {"up": [], "down": [], "left": [], "right": []}
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
