from global_various import *
from collider import Collider


class Player(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        motionful.add(self)
        self.image = load_image(image)
        self.rect_f = list(self.image.get_rect())
        self.rect_f[0] = width / 2 - self.rect_f[2]
        self.rect_f[1] = height / 2 - self.rect_f[3]
        self.rect = pygame.Rect(self.rect_f)
        self.change_x = 0
        self.change_y = 0
        self.speed_run = 300 / FPS
        self.tag = "player"
        self.height_person = self.rect_f[3] * 0.5
        self.player_collider = Collider(self, 0, self.height_person, self.rect_f[2],
                                        self.rect_f[3] - self.height_person)

    def run(self, coord, way):
        if coord == "x":
            self.change_x += self.speed_run * way
        else:
            self.change_y = self.speed_run * way

    def check_pressed(self):
        pressed_btns = pygame.key.get_pressed()
        if pressed_btns[pygame.K_a]:
            self.run("x", -1)
        if pressed_btns[pygame.K_d]:
            self.run("x", 1)
        if pressed_btns[pygame.K_w]:
            self.run("y", -1)
        if pressed_btns[pygame.K_s]:
            self.run("y", 1)

    def change_all_pos(self):
        for i in rooms:
            i.move_camera(self.change_x, self.change_y)
        for i in background:
            i.move_camera(self.change_x, self.change_y)
        for i in motionless:
            i.move_camera(self.change_x, self.change_y)
        for i in motionful:
            if i != self:
                i.move_camera(self.change_x, self.change_y)
        for i in collider_group:
            i.move_camera(self.change_x, self.change_y)

    def check_colliders(self):
        colliders = pygame.sprite.spritecollide(self.player_collider, collider_group, False)
        if colliders:
            for i in colliders:
                i.owner.player_collided(self.player_collider)
