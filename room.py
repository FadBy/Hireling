from camera import Camera
from global_various import *
from wall import Wall
from surface import Surface


class Room:
    def __init__(self, surface_image, wall_images, x, y, w, h, up=[not FULL_CORNER, not FULL_CORNER],
                 down=[FULL_CORNER, FULL_CORNER]):
        rooms.append(self)
        self.height_wall = load_image(wall_images[WALL_SPRITE]).get_rect()[3]
        self.thickness = load_image(wall_images[VERTICAL_SPRITE]).get_rect()[2]
        self.rect_f = [x, y, w * METR + self.thickness * 2, h * METR + self.thickness * 2]
        self.tag = "room"
        self.surface = Surface(self, surface_image, self.thickness, self.thickness, w, h)
        self.walls = {"up": Wall(self, wall_images, 0, 0, w, up),
                      "down": Wall(self, wall_images, 0, self.rect_f[3] - self.thickness, w, down),
                      "left": Wall(self, wall_images[0], 0, 0, h),
                      "right": Wall(self, wall_images[0], self.rect_f[2] - self.thickness, 0, h)}

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
