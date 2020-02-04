from bullet import Bullet
from watchtimer import Timer
from collider import Collider
from functions import *
from character import *
from interface import Interface
from animator import Animator


class Player(Character):
    def __init__(self):
        super().__init__(middle, motionful)
        self.timers = {"weapon": [0.1, self.stop_timer_rapidity], "jerk": [1, self.stop_timer_jerk],
                       "illusion": [0.2, self.stop_timer_illusion], "health": [1, self.stop_timer_damage],
                       "after_jerk": [0.15, self.stop_timer_after_jerk], "after_melle": []}
        self.tag = "player"
        self.image = PLAYER["player_face"]
        self.rect_f = list(self.image.get_rect())
        self.rect_f[X] = width // 2 - self.rect_f[2] // 2
        self.rect_f[Y] = height // 2 - self.rect_f[3] // 2
        self.rect = pygame.Rect(self.rect_f)
        self.height_person = self.rect_f[H] * HEIGHT_UNIT_COLLIDER
        self.colliders = {"default": Collider(self, WIDTH_UNIT_COLLIDER * self.rect_f[W], self.height_person,
                                              self.rect_f[W] - WIDTH_UNIT_COLLIDER * 2 * self.rect[W],
                                              self.rect_f[H] - self.height_person),
                          "bullet_hit": Collider(self, INDENT_UNIT_COLLIDET * self.rect_f[W],
                                                 INDENT_UNIT_COLLIDET * self.rect_f[H],
                                                 self.rect_f[W] - 2 * INDENT_UNIT_COLLIDET * self.rect_f[W],
                                                 self.rect_f[H] - INDENT_UNIT_COLLIDET * self.rect_f[H], True),
                          "collide_with_enemy": Collider(self, WIDTH_UNIT_COLLIDER * self.rect_f[W],
                                                         self.height_person,
                                                         self.rect_f[W] - WIDTH_UNIT_COLLIDER * 2 * self.rect_f[W],
                                                         self.rect_f[H] - self.height_person, True),
                          "zone_melle": Collider(self, self.rect_f[W] * 0.3, -0.15 * self.rect_f[H], self.rect_f[W] * 0.4, self.rect_f[H] * 0.4, True)}


        self.tick = 0
        self.arena = None
        self.change_x = 0
        self.change_y = 0
        self.not_damaged = False
        self.interface = Interface()
        self.full_health = 5
        self.rapidity = False
        self.condition = "stand"
        self.angle = 270
        self.illusions = []
        self.current_length_jerk = 0
        self.test = False
        self.count_set_illusion = 0

        self.animation = []
        self.frame = 0
        self.not_attacking = True

        self.speed = 0
        self.speed_run = 1000
        self.speed_jerk = 1000
        self.length_jerk = 300

        self.damage_bullet = 1
        self.damage_melle = 2

        self.weapon = True
        self.battle = False

        self.not_damaged = False
        self.rapidity = False
        self.jerk_delay = False
        self.after_jerk = False

        self.full_health = 5
        self.health = 5
        self.bandolier = 0
        self.ammo_in_magazine = 0
        self.full_ammo = 0
        self.interface = Interface(self)

        self.active_animation = None
        self.animation_attack_melee_up = Animator(self, [PLAYER["player_back1"], PLAYER["player_back2"],
                                                      PLAYER["player_back3"], PLAYER["player_back201"]], PLAYER["player_back1"], 0.5)

    def move(self, x, y):
        self.change_x += x * self.tick
        self.change_y += y * self.tick

    def move_by_collider(self, x, y):
        if x != 0:
            self.change_x = x
        if y != 0:
            self.change_y = y

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
        self.current_length_jerk += self.speed_jerk * self.tick
        coord = set_change_coord(self.angle, self.speed_jerk)
        self.move(*coord)

    def run(self, side):
        self.condition = "run"
        self.angle = convert_side_in_angle(side)
        if pygame.key.get_pressed()[pygame.K_SPACE] and not self.jerk_delay:
            self.jerk()
        else:
            coord = set_change_coord(self.angle, self.speed_run)
            self.move(*coord)

    def stop_timer_jerk(self):
        self.jerk_delay = False

    def stop_timer_damage(self):
        self.not_damaged = False

    def attack(self, attacked_side):
        if self.weapon:
            if not self.rapidity:
                self.ammo_in_magazine -= 1
                if self.interface.changes(self.interface.health, self.ammo_in_magazine) != 'empty':
                    self.ammo_in_magazine = self.interface.ammo_in_magazine
                    self.rapidity = True
                    Timer(*self.timers["weapon"]).start()
                    bullet = Bullet(self, convert_side_in_angle(attacked_side))
        if (not self.weapon or self.interface.ammo_in_magazine == 0) and self.not_attacking:
            if attacked_side == 'up':
                colliders = pygame.sprite.spritecollide(self.colliders["zone_melle"], enemies, False)
                if not self.animation_attack_melee_up.started:
                    for i in colliders:
                        if pygame.sprite.collide_rect(self.colliders["zone_melle"], i.colliders["collide_with_enemy"]):
                            i.hit_from_enemy(self.damage_melle)
                self.animation_attack_melee_up.start()

    def check_pressed(self):
        if not self.condition == "jerk":
            if not self.after_jerk:
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
                if movement_buttons["a"] and movement_buttons["d"] and movement_buttons["w"]:
                    print()
                if pressed_btns[pygame.K_ESCAPE]:
                    return ingame_menu_start()
                if movement_buttons["a"] and not movement_buttons["w"] and not movement_buttons["s"]:
                    self.image = PLAYER["player_left"]
                    self.run("left")
                if movement_buttons["d"] and not movement_buttons["w"] and not movement_buttons["s"]:
                    self.image = PLAYER["player_right"]
                    self.run("right")
                if movement_buttons["w"] and not movement_buttons["a"] and not movement_buttons["d"]:
                    self.image = PLAYER["player_back1"]
                    self.run("up")
                if movement_buttons["s"] and not movement_buttons["a"] and not movement_buttons["d"]:
                    self.image = PLAYER["player_face"]
                    self.run("down")
                if movement_buttons["d"] and movement_buttons["w"]:
                    self.run("right-up")
                if movement_buttons["a"] and movement_buttons["w"]:
                    self.run("left-up")
                if movement_buttons["a"] and movement_buttons["s"]:
                    self.run("left-down")
                if movement_buttons["d"] and movement_buttons["s"]:
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

    def hit_from_collider(self, hp):
        self.condition = 'stand'
        if not self.not_damaged:
            self.interface.health -= hp
            self.not_damaged = True
            Timer(*self.timers["health"]).start()
            self.interface.changes(self.interface.health, self.interface.ammo_in_magazine)

    def heal(self, hp):
        if self.interface.health < self.full_health:
            self.interface.health += 1
            self.interface.changes(self.interface.health, self.interface.ammo_in_magazine)

    def hit_from_enemy(self, hp):
        self.interface.health -= hp
        self.interface.changes(self.interface.health, self.interface.ammo_in_magazine)

    def unit_collided(self, collider, unit):
        pass
        if unit.owner.tag == "enemy" and collider == self.colliders["collide_with_enemy"] and unit == \
                unit.owner.colliders["collide_with_enemy"]:
            self.hit_from_collider(unit.owner.damage_collide)

    def set_arena(self, arena):
        self.arena = arena
