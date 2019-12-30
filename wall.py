from camera import Camera
from global_various import *
from collider import Collider


class Wall(Camera):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = load_image(image)
        self.rect_f = list(self.image.get_rect())
        self.rect_f[0], self.rect_f[1] = x, y
        self.rect = pygame.Rect(*self.rect_f)
        self.tag = "wall"

        if self.rect[2] > self.rect[3]:
            self.add(walls_hor_group)
            self.way = "horisontal"
            self.collider = Collider(self, x, y, self.rect_f[2],
                                     self.rect_f[3])
            self.collider.add()
        else:
            walls_ver_group.add(self)
            self.way = "vertical"
            self.collider = Collider(self, x, y, self.rect[2],
                                     self.rect_f[3])

    def move_camera(self, x, y):
        super().move_camera(x, y)
        self.collider.change_pos(x, y)

    def player_collided(self, player):
        if player.tag == "player":
            if player.change_x > 0 and player.change_y == 0:
                player.change_x = self.rect_f[0] - player.rect_f[0] - player.rect_f[2]
            elif player.change_x < 0 and player.change_y == 0:
                player.change_x = self.rect_f[0] + self.rect_f[2] - player.rect_f[0]
            elif player.change_x == 0 and player.change_y > 0:
                player.change_y = self.rect_f[1] - player.rect[1] - player.rect_f[3]
            elif player.change_x == 0 and player.change_y < 0:
                player.change_y = self.rect_f[1] + self.rect_f[3] - player.rect_f[1]
            elif player.rect_f[0] < self.rect_f[0] and player.rect_f[1] > self.rect_f[1] and \
                    player.rect_f[1] + player.rect_f[3] < self.rect_f[1] + self.rect_f[3]:
                player.change_x = self.rect_f[0] - player.rect_f[0] - player.rect_f[2]
            elif player.rect_f[0] + player.rect_f[2] > self.rect_f[0] + self.rect_f[2] and \
                    player.rect_f[1] > self.rect_f[1] and \
                    player.rect_f[1] + player.rect_f[3] < self.rect_f[1] + self.rect_f[3]:
                player.change_x = self.rect_f[0] + self.rect_f[2] - player.rect_f[0]
            elif player.rect_f[1] < self.rect_f[1] and player.rect_f[0] > self.rect_f[0] and \
                    player.rect_f[0] < self.rect_f[0] + self.rect_f[2]:
                player.change_y = self.rect_f[1] - player.rect[1] - player.rect_f[3]
            elif player.rect_f[1] + player.rect_f[3] > self.rect_f[1] and player.rect_f[
                0] > \
                    self.rect_f[0] and player.rect_f[0] + player.rect_f[2] < self.rect_f[0] + \
                    self.rect_f[2]:
                player.change_y = self.rect_f[1] + self.rect_f[3] - player.rect_f[1]
