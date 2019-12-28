from camera import Camera
from global_various import *


class Player(pygame.sprite.Sprite):
    def __init__(self, image="player.png"):
        super().__init__()
        self.image = load_image(image)
        player_group.add(self)
        self.rect = [width // 2, height // 2, *self.image.get_rect()[2:]]
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
        for i in motionless:
            for j in i:
                j.move_camera(self.change_x, self.change_y)
        for i in motionful:
            for j in i:
                if j != self:
                    j.move_camera(self.change_x, self.change_y)
        self.change_x = 0
        self.change_y = 0
