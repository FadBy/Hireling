from all_various import *
from collider import Collider
from sprite import Sprite
from bullet import Bullet


class Player(Sprite):
    def __init__(self):
        super().__init__(middle, motionful)
        self.animation = []
        self.image = PLAYER["player_face"]
        self.rect_f = list(self.image.get_rect())
        self.rect_f[X] = width // 2 - self.rect_f[2]
        self.rect_f[Y] = height // 2 - self.rect_f[3]
        self.rect = pygame.Rect(self.rect_f)
        self.change_x = 0
        self.change_y = 0
        self.speed_run = 150
        self.tag = "player"
        self.bullets = []
        self.height_person = self.rect_f[H] * WIDTH_UNIT_COLLIDER
        self.collider = Collider(self, 0, self.height_person, self.rect_f[W],
                                        self.rect_f[H] - self.height_person)
        self.frame = 0
        self.not_attacking = True
        self.tick = None
        self.weapon = True
        self.change_x = 0
        self.change_y = 0

    def move(self, x, y):
        self.change_x += x * self.tick
        self.change_y += y * self.tick

    def set_tick(self, tick):
        self.tick = tick

    def run(self, coord, way):
        if coord == "x":
            self.move(self.speed_run * way, 0)
        else:
            self.move(0, self.speed_run * way)

    def attack(self, weapon_type, attacked_side):
        if self.weapon:
            if attacked_side == "right":
                self.bullets.append(Bullet(self, 0))
            elif attacked_side == "up":
                self.bullets.append(Bullet(self, 90))
            elif attacked_side == "left":
                self.bullets.append(Bullet(self, 180))
            else:
                self.bullets.append(Bullet(self, 270))

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

    def check_colliders(self):
        colliders = pygame.sprite.spritecollide(self.player_collider, collider_group, False)
        if colliders:
            for i in colliders:
                if i.owner != self:
                    if not i.trigger:
                        i.default_collide(self.player_collider)
                    else:
                        i.owner.unit_collided()
