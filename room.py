from camera import Camera
from all_various import *
from wall import Wall
from surface import Surface


class Room:
    def __init__(self, images, x, y, w, h, doors, up=[not FULL_CORNER, not FULL_CORNER],
                 down=[FULL_CORNER, FULL_CORNER]):
        rooms.append(self)
        self.height_wall = images["wall_block_hor"].get_rect()[3]
        self.thickness = images["wall_block_ver"].get_rect()[2]
        self.rect_f = [x, y, w * METR + self.thickness * 2, h * METR + self.thickness * 2]
        self.tag = "room"
        self.walls = {}
        for i in range(len(doors)):
            if doors[i][0] == "up":
                self.walls["up"] = Wall(self, "horisontal", images, 0, 0, w, doors[i][1:], up)
            elif doors[i][0] == "down":
                self.walls["down"] = Wall(self, "horisontal", images, 0, self.rect_f[3] - self.thickness, w,
                                          doors[i][1:], down)
            elif doors[i][0] == "left":
                self.walls["left"] = Wall(self, "vertical", images, 0, 0, h, doors[i][1:])
            else:
                self.walls["right"] = Wall(self, "vertical", images, self.rect_f[2] - self.thickness, 0, h,
                                           doors[i][1:])
        if "up" not in self.walls:
            self.walls["up"] = Wall(self, "horisontal", images, 0, 0, w, [], up)
        if "down" not in self.walls:
            self.walls["down"] = Wall(self, "horisontal", images, 0, self.rect_f[3] - self.thickness, w, [], down)
        if "left" not in self.walls:
            self.walls["left"] = Wall(self, "vertical", images, 0, 0, h, [])
        if "right" not in self.walls:
            self.walls["right"] = Wall(self, "vertical", images, self.rect_f[2] - self.thickness, 0, h, [])
        self.surface = Surface(self, images, self.thickness, self.thickness, w, h)

    def move_camera(self, x, y):
        self.rect_f[0] -= x
        self.rect_f[1] -= y
        self.surface.move_camera(x, y)
        for i in self.walls:
            self.walls[i].move_camera(x, y)

    def draw(self, screen):
        self.surface.draw(screen)
        for i in self.walls:
            self.walls[i].draw(screen)
