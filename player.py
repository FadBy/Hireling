from bullet import Bullet
from watchtimer import Timer
from collider import Collider
from functions import *
from character import *
from interface import Interface


class Player(Character):
    def __init__(self):
        super().__init__(middle, motionful)
        self.timers = {"weapon": [0.3, self.stop_timer_rapidity], "jerk": [1, self.stop_timer_jerk],
                       "illusion": [0.2, self.stop_timer_illusion], "health": [1, self.stop_timer_damage],
                       "after_jerk": [0.15, self.stop_timer_after_jerk]}
        self.animation = []
        self.image = PLAYER["player_face"]
        self.rect_f = list(self.image.get_rect())
        self.rect_f[X] = width // 2 - self.rect_f[2] // 2
        self.rect_f[Y] = height // 2 - self.rect_f[3] // 2
        self.rect = pygame.Rect(self.rect_f)
        self.speed_run = 1000
        self.tag = "player"
        self.height_person = self.rect_f[H] * HEIGHT_UNIT_COLLIDER
        self.colliders.append(Collider(self, WIDTH_UNIT_COLLIDER * self.rect_f[W], self.height_person,
                                       self.rect_f[W] - WIDTH_UNIT_COLLIDER * 2 * self.rect_f[W],
                                       self.rect_f[H] - self.height_person))
        self.colliders.append(
            Collider(self, INDENT_UNIT_COLLIDET * self.rect_f[W], INDENT_UNIT_COLLIDET * self.rect_f[H],
                     self.rect_f[W] - 2 * INDENT_UNIT_COLLIDET * self.rect_f[W],
                     self.rect_f[H] - 2 * INDENT_UNIT_COLLIDET * self.rect_f[H], True))

        self.bullets = []
        self.frame = 0
        self.length_jerk = 300
        self.speed_jerk = 1000
        self.not_attacking = True
        self.tick = 0
        self.change_x = 0
        self.change_y = 0
        self.health = 5
        self.not_damaged = False
        self.full_health = 5
        self.rapidity = False
        self.condition = "stand"
        self.angle = 270
        self.jerk_delay = False
        self.illusions = []
        self.current_length_jerk = 0
        self.test = False
        self.count_set_illusion = 0
        self.after_jerk = False
        self.weapon = True
        self.interface = Interface()

    def move(self, speed):
        if self.condition == "jerk":
            self.current_length_jerk += speed * self.tick
        coord = set_change_coord(self.angle, speed)
        self.change_x += coord[X] * self.tick
        self.change_y += coord[Y] * self.tick

    def stop_timer_illusion(self):
        self.illusions[0].kill()

    def stop_timer_after_jerk(self):
        self.after_jerk = False

    def jerk(self):
        self.condition = "jerk"
        if self.current_length_jerk >= self.length_jerk / COUNT_OF_ILLUSIONS * self.count_set_illusion:
            self.count_set_illusion += 1
            illussion = Sprite(object_sprites, middle, self.illusions)
            illussion.image = self.image
            illussion.rect_f = self.rect_f.copy()
            Timer(*self.timers['illusion']).start()
        if self.current_length_jerk >= self.length_jerk:
            self.after_jerk = True
            self.count_set_illusion = 0
            self.condition = "stand"
            self.jerk_delay = True
            self.current_length_jerk = 0
            Timer(*self.timers["after_jerk"]).start()
            Timer(*self.timers["jerk"]).start()
        self.move(self.speed_jerk)

    def run(self, side):
        self.condition = "run"
        self.angle = convert_side_in_angle(side)
        if pygame.key.get_pressed()[pygame.K_SPACE] and not self.jerk_delay:
            self.jerk()
        else:
            self.move(self.speed_run)

    def stop_timer_jerk(self):
        self.jerk_delay = False

    def stop_timer_damage(self):
        self.not_damaged = False

    def attack(self, attacked_side):
        if self.weapon:
            if not self.rapidity:
                self.rapidity = True
                Timer(*self.timers["weapon"]).start()
                bullet = Bullet(self, convert_side_in_angle(attacked_side))
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
                    if not self.weapon:
                        self.not_attacking = False
                    self.frame = 0

    def check_pressed(self):
        if not self.condition == "jerk":
            if not self.after_jerk:
                self.condition = "stand"
                pressed_btns = pygame.key.get_pressed()
                self.image = PLAYER["player_face"]
                if pressed_btns[pygame.K_ESCAPE]:
                    return ingame_menu_start()
                if pressed_btns[pygame.K_a] and not pressed_btns[pygame.K_w] and not pressed_btns[
                    pygame.K_s]:
                    self.image = PLAYER["player_left"]
                    self.run("left")
                if pressed_btns[pygame.K_d] and not pressed_btns[pygame.K_w] and not pressed_btns[
                    pygame.K_s]:
                    self.image = PLAYER["player_right"]
                    self.run("right")
                if pressed_btns[pygame.K_w] and not pressed_btns[pygame.K_a] and not pressed_btns[
                    pygame.K_d]:
                    self.image = PLAYER["player_back1"]
                    self.run("up")
                if pressed_btns[pygame.K_s] and not pressed_btns[pygame.K_a] and not pressed_btns[
                    pygame.K_d]:
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
                    self.attack("left-up")
                elif pressed_btns[pygame.K_LEFT] and pressed_btns[pygame.K_DOWN]:
                    self.attack("left-down")
                elif pressed_btns[pygame.K_RIGHT] and pressed_btns[pygame.K_UP]:
                    self.attack('right-up')
                elif pressed_btns[pygame.K_RIGHT] and pressed_btns[pygame.K_DOWN]:
                    self.attack("right-down")
                elif pressed_btns[pygame.K_LEFT]:
                    self.attack('left')
                elif pressed_btns[pygame.K_RIGHT]:
                    self.attack('right')
                elif pressed_btns[pygame.K_UP]:
                    self.attack('up')
                elif pressed_btns[pygame.K_DOWN]:
                    self.attack('down')
                else:
                    self.frame = 0
                    self.not_attacking = True
        else:
            self.jerk()
        return ''

    def hit_from_enemy(self, hp):
        self.condition = 'stand'
        if not self.not_damaged:
            self.health -= hp
            self.not_damaged = True
            Timer(*self.timers["health"]).start()
            self.interface.change_hp(self.health)

    def unit_collided(self, unit):
        if unit.owner.tag == "bullet" and unit.owner.owner.tag != "player":
            self.hit_from_enemy(unit.owner.owner.damage_bullet)
