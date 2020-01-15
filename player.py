from all_various import *
from collider import Collider


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        motionful.add(self)
        self.animation = []
        self.image = PLAYER["player_face"]
        self.rect_f = list(self.image.get_rect())
        self.rect_f[0] = width / 2 - self.rect_f[2]
        self.rect_f[1] = height / 2 - self.rect_f[3]
        self.rect = pygame.Rect(self.rect_f)
        self.change_x = 0
        self.change_y = 0
        self.speed_run = 150
        self.tag = "player"

        self.height_person = self.rect_f[3] * WIDTH_UNIT_COLLIDER
        self.player_collider = Collider(self, 0, self.height_person, self.rect_f[2],
                                        self.rect_f[3] - self.height_person)
        self.frame = 0
        self.not_attacking = True
        self.tick = None

    def set_tick(self, tick):
        self.tick = tick

    def run(self, coord, way):
        if coord == "x":
            self.change_x += self.speed_run * way * self.tick
        else:
            self.change_y = self.speed_run * way * self.tick

    def attack(self, weapon_type, attacked_side):
        if self.not_attacking:
            if attacked_side == 'up':
                fst, snd, trd, fth = PLAYER["player_back1"], PLAYER["player_back2"], \
                                PLAYER["player_back201"], PLAYER["player_back3"]
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
        self.image = PLAYER["player_face"]
        if pressed_btns[pygame.K_a]:
            self.run("x", -1)
        if pressed_btns[pygame.K_d]:
            self.run("x", 1)
        if pressed_btns[pygame.K_w]:
            self.run("y", -1)
            self.image = PLAYER["player_back1"]
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
        return ''

    def change_all_pos(self):
        for i in rooms:
            i.move_camera(self.change_x, self.change_y)

    def check_colliders(self):
        colliders = pygame.sprite.spritecollide(self.player_collider, motionless_collider_group, False)
        if colliders:
            for i in colliders:
                if not i.trigger:
                    i.default_collide(self.player_collider)
                else:
                    i.owner.unit_collided()

    def draw(self, screen):
        screen.blit(self.image, self.rect)