from camera import Camera
from global_various import *


class Player(Camera):
    def __init__(self):
        super().__init__()
        self.image = load_image("player.png", -1)
        self.set_pos((width // 2, height // 2))
        self.set_rect(self.image.get_rect())
        self.change_x = 0
        self.change_y = 0
        self.speed_run = 1000 // FPS

    def run(self, coord, way):
        if coord == 0:
            self.change_x += self.speed_run * way
        else:
            self.change_y = self.speed_run * way

    def check_pressed(self):
        pressed_btns = pygame.key.get_pressed()
        if pressed_btns[pygame.K_a]:
            self.run(0, -1)
        if pressed_btns[pygame.K_d]:
            self.run(0, 1)
        if pressed_btns[pygame.K_w]:
            self.run(1, -1)
        if pressed_btns[pygame.K_s]:
            self.run(1, 1)

    def change_all_pos(self):
        for i in self.all_sprites:
            i.move_camera(self.change_x, self.change_y)
        self.change_x = 0
        self.change_y = 0
