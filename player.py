from watchtimer import Timer
from character import *
from interface import Interface
from animator import Animator
from melle import Melle
from pistol import Pistol
from functions import *
from collider import Collider


class Player(Character):
    def __init__(self):
        super().__init__(middle, motionful)
        self.timers = {"weapon": [0.1, self.stop_timer_rapidity], "jerk": [1, self.stop_timer_jerk],
                       "illusion": [0.2, self.stop_timer_illusion], "health": [1, self.stop_timer_damage],
                       "after_jerk": [0.15, self.stop_timer_after_jerk], "after_melle": []}
        self.tag = "player"
        self.image = PLAYER["player_face"]
        self.rect_f = list(self.image.get_rect())
        self.rect_f[X] = width // 2 - self.rect_f[W] // 2
        self.rect_f[Y] = height // 2 - self.rect_f[H] // 2
        self.rect = pygame.Rect(self.rect_f)
        self.height_person = self.rect_f[H] * HEIGHT_UNIT_COLLIDER
        self.layer_collider = 1
        self.colliders = {"bullet_hit": Collider(self, INDENT_UNIT_COLLIDET * self.rect_f[W],
                                                 INDENT_UNIT_COLLIDET * self.rect_f[H],
                                                 self.rect_f[W] - 2 * INDENT_UNIT_COLLIDET * self.rect_f[W],
                                                 self.rect_f[H] - INDENT_UNIT_COLLIDET * self.rect_f[H], True),
                          "collide_with_enemy": Collider(self, WIDTH_UNIT_COLLIDER * self.rect_f[W],
                                                         self.height_person,
                                                         self.rect_f[W] - WIDTH_UNIT_COLLIDER * 2 * self.rect_f[W],
                                                         self.rect_f[H] - self.height_person, True),
                          }
        if not NOCLIP:
            self.colliders["default"] = Collider(self, WIDTH_UNIT_COLLIDER * self.rect_f[W], self.height_person,
                                                 self.rect_f[W] - WIDTH_UNIT_COLLIDER * 2 * self.rect[W],
                                                 self.rect_f[H] - self.height_person)
        self.tick = 0
        self.passed_rooms = 0
        self.arena = None
        self.change_x = 0
        self.change_y = 0
        self.condition = "stand"
        self.angle = 270
        self.illusions = []
        self.current_length_jerk = 0
        self.count_set_illusion = 0
        self.step_stop = 0
        self.max_steps = 8
        self.min_steps = 0

        self.speed = 0

        if GOD:
            self.speed_run = 1000
        else:
            self.speed_run = 500
        self.speed_jerk = 1000
        self.length_jerk = 300

        self.weapons = [Melle(self), Pistol(self)]
        self.weapon = self.weapons[0]
        self.battle = False

        self.not_damaged = False
        self.rapidity = False
        self.jerk_delay = False
        self.after_jerk = False
        if GOD:
            self.full_health = 100
            self.health = 100
        else:
            self.full_health = 5
            self.health = 5

        self.difficult = 1

        self.sort_process = False

        self.interface = Interface(self)

        self.animation_attack_melee_up = Animator(self, [PLAYER["player_back1"], PLAYER["player_back2"],
                                                         PLAYER["player_back3"], PLAYER["player_back201"],
                                                         PLAYER["player_back1"]],
                                                  PLAYER["player_back1"], 0.5)
        self.animation_run_back = Animator(self, [PLAYER["player_back_run_1"], PLAYER["player_back_run_2"],
                                                  PLAYER["player_back_run_3"], PLAYER["player_back_run_4"],
                                                  PLAYER["player_back_run_5"]], PLAYER["player_back1"], 0.75)
        self.animation_run_face = Animator(self, [PLAYER["player_face_run_1"], PLAYER["player_face_run_2"],
                                                  PLAYER["player_face_run_3"], PLAYER["player_face_run_4"]],
                                           PLAYER["player_face"], 0.75)
        self.animation_run_right = Animator(self, [PLAYER["player_right_run_1"], PLAYER["player_right_run_2"],
                                                   PLAYER["player_right_run_3"], PLAYER["player_right_run_4"],
                                                   PLAYER["player_right_run_5"], PLAYER["player_right_run_6"]],
                                            PLAYER["player_right"], 0.75)
        self.animation_run_left = Animator(self, [PLAYER["player_left_run_1"], PLAYER["player_left_run_2"],
                                                  PLAYER["player_left_run_3"], PLAYER["player_left_run_4"],
                                                  PLAYER["player_left_run_5"], PLAYER["player_left_run_6"]],
                                           PLAYER["player_left"], 0.75)
        self.active_animation = self.animation_run_face

    def move(self, x, y):
        self.change_x += x * self.tick
        self.change_y += y * self.tick

    def death(self):
        self.__init__()

    def move_by_collider(self, x, y):
        if x != 0:
            self.change_x = x
        if y != 0:
            self.change_y = y

    def delete_illusion(self, ilus):
        if ilus in middle:
            middle.remove(ilus)
        if ilus in object_sprites:
            object_sprites.remove(ilus)
        if ilus in self.illusions:
            self.illusions.remove(ilus)

    def stop_timer_illusion(self):
        if len(self.illusions) != 0:
            middle.remove(self.illusions[0])
            object_sprites.remove(self.illusions[0])
            del self.illusions[0]

    def stop_timer_after_jerk(self):
        self.after_jerk = False
        for i in self.illusions:
            self.delete_illusion(self.illusions[0])

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
        self.current_length_jerk += self.speed_jerk * self.tick
        coord = set_change_coord(self.angle, self.speed_jerk)
        self.move(*coord)

    def run(self, side):
        self.condition = "run"
        self.angle = convert_side_in_angle(side)
        if pygame.key.get_pressed()[pygame.K_SPACE] and not self.jerk_delay:
            blink.play()
            self.jerk()
        else:
            coord = set_change_coord(self.angle, self.speed_run)
            self.move(*coord)
            if self.step_stop == 0:
                steps.play()
                self.step_stop += 1
            elif self.min_steps < self.step_stop < self.max_steps:
                self.step_stop += 1
            else:
                self.step_stop = 0

    def stop_timer_jerk(self):
        self.jerk_delay = False

    def stop_timer_damage(self):
        self.not_damaged = False

    def attack(self, attacked_side):
        if not self.rapidity:
            self.weapon.shoot(convert_side_in_angle(attacked_side))

    def load_bullets(self):
        for i in self.weapons:
            if i.shootable:
                i.load_bullets()
        self.interface.set_ammo()

    def check_pressed(self):
        if not self.condition == "jerk":
            if not self.after_jerk:
                for i in self.illusions:
                    i.kill()
                self.condition = "stand"
                pressed_btns = pygame.key.get_pressed()
                movement_buttons = {"a": False, "w": False, "d": False, "s": False}
                if pressed_btns[pygame.K_a] and not pressed_btns[pygame.K_d]:
                    movement_buttons["a"] = True
                if pressed_btns[pygame.K_w] and not pressed_btns[pygame.K_s]:
                    movement_buttons["w"] = True
                if pressed_btns[pygame.K_d] and not pressed_btns[pygame.K_a]:
                    movement_buttons["d"] = True
                if pressed_btns[pygame.K_s] and not pressed_btns[pygame.K_w]:
                    movement_buttons["s"] = True
                if pressed_btns[pygame.K_r]:
                    self.weapon.reload()
                if pressed_btns[pygame.K_ESCAPE]:
                    return ingame_menu_start()
                if movement_buttons["a"] and not movement_buttons["w"] and not movement_buttons["s"]:
                    self.change_animation(self.animation_run_left)
                    self.run("left")
                if movement_buttons["d"] and not movement_buttons["w"] and not movement_buttons["s"]:
                    self.change_animation(self.animation_run_right)
                    self.run("right")
                if movement_buttons["w"] and not movement_buttons["a"] and not movement_buttons["d"]:
                    self.change_animation(self.animation_run_back)
                    self.run("up")
                if movement_buttons["s"] and not movement_buttons["a"] and not movement_buttons["d"]:
                    self.change_animation(self.animation_run_face)
                    self.run("down")
                if not movement_buttons["s"] and not movement_buttons["w"] and not movement_buttons["d"] and not \
                        movement_buttons["a"]:
                    if self.active_animation != self.animation_attack_melee_up:
                        self.active_animation.cancel()
                        self.image = self.active_animation.default
                if movement_buttons["d"] and movement_buttons["w"]:
                    self.active_animation.start()
                    self.run("right-up")
                if movement_buttons["a"] and movement_buttons["w"]:
                    self.active_animation.start()
                    self.run("left-up")
                if movement_buttons["a"] and movement_buttons["s"]:
                    self.active_animation.start()
                    self.run("left-down")
                if movement_buttons["d"] and movement_buttons["s"]:
                    self.active_animation.start()
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
                if pressed_btns[pygame.K_1]:
                    self.weapon = self.weapons[0]
                    self.interface.set_ammo()
                    self.interface.set_weapon()
                elif pressed_btns[pygame.K_2]:
                    self.weapon = self.weapons[1]
                    self.interface.set_ammo()
                    self.interface.set_weapon()
                elif pressed_btns[pygame.K_3]:
                    if len(self.weapons) > 2:
                        self.weapon = self.weapons[2]
                        self.interface.set_ammo()
                        self.interface.set_weapon()
                elif pressed_btns[pygame.K_4]:
                    if len(self.weapons) > 3:
                        self.weapon = self.weapons[3]
                        self.interface.set_ammo()
                        self.interface.set_weapon()
        else:
            self.jerk()
        return ''

    def hit_from_collider(self, hp):
        self.condition = 'stand'
        if not self.not_damaged:
            self.health -= hp
            self.not_damaged = True
            Timer(*self.timers["health"]).start()
            self.interface.change_hp()

    def heal(self, hp):
        if self.health + hp < self.full_health:
            self.health += hp
        else:
            self.health = self.full_health
        self.interface.change_hp()

    def hit_from_enemy(self, hp):
        if self.condition != "jerk":
            self.health -= hp
            self.interface.change_hp()

    def unit_collided(self, collider, unit):
        pass
        if unit.owner.tag == "enemy" and collider == self.colliders["collide_with_enemy"] and unit == \
                unit.owner.colliders["collide_with_enemy"] and self.condition != "jerk":
            self.hit_from_collider(unit.owner.damage_collide)

    def set_arena(self, arena):
        self.arena = arena
