from collider import *
from sprite import *
from bullet import *
from various import *
from watchtimer import Timer
from sprites import *


class Player(Sprite):
    def __init__(self):
        super().__init__(middle, motionful, timers_with)
        self.timers = {"weapon": [0.3, self.stop_timer_rapidity], "jerk": [1, self.stop_timer_jerk],
                       "illusion": [0.1, self.stop_timer_illusion]}
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
        self.height_person = self.rect_f[H] * WIDTH_UNIT_COLLIDER
        self.collider = Collider(self, 0, self.height_person, self.rect_f[W],
                                 self.rect_f[H] - self.height_person)
        self.frame = 0
        self.length_jerk = 150
        self.speed_jerk = 1000
        self.not_attacking = True
        self.tick = None
        self.weapon = True
        self.change_x = 0
        self.change_y = 0
        self.rapidity = False
        self.condition = "stand"
        self.angle = 270
        self.jerk_delay = False
        self.illusions = []
        self.current_length_jerk = 0

    def move(self, speed):
        if self.condition == "jerk":
            self.current_length_jerk += speed * self.tick
            # print(self.current_length_jerk, "+=", speed, " * ", self.tick)
        if self.angle % 90 == 0:
            if self.angle % 360 == 0:
                x = speed
                y = 0
            elif self.angle % 360 == 90:
                x = 0
                y = -speed
            elif self.angle % 360 == 180:
                x = -speed
                y = 0
            else:
                x = 0
                y = speed
        elif self.angle % 45 == 0:
            if self.angle == 45:
                x = speed * sin(pi / 4)
                y = -speed * sin(pi / 4)
            elif self.angle == 135:
                x = -speed * sin(pi / 4)
                y = -speed * sin(pi / 4)
            elif self.angle == 225:
                x = -speed * sin(pi / 4)
                y = speed * sin(pi / 4)
            else:
                x = speed * sin(pi / 4)
                y = speed * sin(pi / 4)
        self.change_x += x * self.tick
        self.change_y += y * self.tick

    def stop_timer_illusion(self):
        self.illusions[0].kill()
        print(len(self.illusions))

    def set_tick(self, tick):
        self.tick = tick

    def jerk(self):
        self.condition = "jerk"
        if self.current_length_jerk >= self.length_jerk / COUNT_OF_ILLUSIONS * len(self.illusions):
            illussion = Sprite(object_sprites, middle, self.illusions)
            illussion.image = self.image
            illussion.rect_f = self.rect_f.copy()
            Timer(*self.timers['illusion']).start()
        if self.current_length_jerk >= self.length_jerk:
            self.condition = "stand"
            self.jerk_delay = True
            self.current_length_jerk = 0
            Timer(*self.timers["jerk"]).start()
        self.move(self.speed_jerk)

    def run(self, side):
        self.condition = "run"
        self.angle = self.convert_side_in_angle(side)
        if pygame.key.get_pressed()[pygame.K_SPACE] and not self.jerk_delay:
            self.jerk()
        else:
            self.move(self.speed_run)

    def convert_side_in_angle(self, side):
        if side == "right":
            return 0
        elif side == "up":
            return 90
        elif side == "left":
            return 180
        elif side == "down":
            return 270
        elif side == "right-up":
            return 45
        elif side == "left-up":
            return 135
        elif side == "left-down":
            return 225
        elif side == "right-down":
            return 315

    def stop_timer_jerk(self):
        self.jerk_delay = False

    def stop_timer_rapidity(self):
        self.rapidity = False

    def attack(self, weapon_type, attacked_side):
        if self.weapon:
            if not self.rapidity:
                self.rapidity = True
                Timer(*self.timers["weapon"]).start()
                bullet = Bullet(self, self.convert_side_in_angle(attacked_side))
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
        if not self.condition == "jerk":
            self.condition = "stand"
            pressed_btns = pygame.key.get_pressed()
            self.image = PLAYER["player_face"]
            if pressed_btns[pygame.K_a] and not pressed_btns[pygame.K_w] and not pressed_btns[pygame.K_s]:
                self.run("left")
            if pressed_btns[pygame.K_d] and not pressed_btns[pygame.K_w] and not pressed_btns[pygame.K_s]:
                self.run("right")
            if pressed_btns[pygame.K_w] and not pressed_btns[pygame.K_a] and not pressed_btns[pygame.K_d]:
                self.run("up")
                self.image = PLAYER["player_back1"]
            if pressed_btns[pygame.K_s] and not pressed_btns[pygame.K_a] and not pressed_btns[pygame.K_d]:
                self.run("down")
            if pressed_btns[pygame.K_d] and pressed_btns[pygame.K_w]:
                self.run("right-up")
            if pressed_btns[pygame.K_a] and pressed_btns[pygame.K_w]:
                self.run("left-up")
            if pressed_btns[pygame.K_a] and pressed_btns[pygame.K_s]:
                self.run("left-down")
            if pressed_btns[pygame.K_d] and pressed_btns[pygame.K_s]:
                self.run("right-down")
            if pressed_btns[pygame.K_LEFT] and pressed_btns[pygame.K_UP]:
                self.attack(False, "left-up")
            elif pressed_btns[pygame.K_LEFT] and pressed_btns[pygame.K_DOWN]:
                self.attack(False, "left-down")
            elif pressed_btns[pygame.K_RIGHT] and pressed_btns[pygame.K_UP]:
                self.attack(False, 'right-up')
            elif pressed_btns[pygame.K_RIGHT] and pressed_btns[pygame.K_DOWN]:
                self.attack(False, "right-down")
            elif pressed_btns[pygame.K_LEFT]:
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
        else:
            self.jerk()
