from global_various import *
from collider import Collider


class Player(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        motionful.add(self)
        self.animation = []
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
        self.frame = 0
        self.not_attacking = True

    def run(self, coord, way):
        if coord == "x":
            self.change_x += self.speed_run * way
        else:
            self.change_y = self.speed_run * way

    def attack(self, weapon_type, attacked_side):
        if self.not_attacking:
            if attacked_side == 'up':
                fst, snd, trd, fth = load_image('player_back1.png'), load_image('player_back2.png'), \
                                load_image('player_back201.png'), load_image('player_back3.png')
                self.animation = []
                for i in range(2):
                    self.animation.append(snd)
                for i in range(2):
                    self.animation.append(trd)
                for i in range(3):
                    self.animation.append(fth)
                self.image = self.animation[self.frame]
                if self.frame < len(self.animation) - 1:
                    self.frame += 1
                else:
                    if not weapon_type:
                        self.not_attacking = False
                    self.frame = 0

    def check_pressed(self):
        pressed_btns = pygame.key.get_pressed()
        self.image = load_image('player_face.png')
        if pressed_btns[pygame.K_a]:
            self.run("x", -1)
        if pressed_btns[pygame.K_d]:
            self.run("x", 1)
        if pressed_btns[pygame.K_w]:
            self.run("y", -1)
            self.image = load_image('player_back1.png')
        if pressed_btns[pygame.K_s]:
            self.run("y", 1)
        if pressed_btns[pygame.K_LEFT]:
            self.attack(False, 'left')
        elif pressed_btns[pygame.K_RIGHT]:
            self.attack(False, 'right')
        elif pressed_btns[pygame.K_UP]:
            self.attack(False, 'up')
        elif pressed_btns[pygame.K_DOWN]:
            self.attack(False, 'down')
        elif pressed_btns[pygame.K_ESCAPE]:
            return 'paused'
        else:
            self.frame = 0
            self.not_attacking = True

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

    def draw(self, screen):
        screen.blit(self.image, self.rect)