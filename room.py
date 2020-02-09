from wall import Wall
from surface import Surface
from various import *
from sprites import *
from collider import Collider
from random import randint
from sprite import Sprite
from watchtimer import Timer
from aid_kit import Aid
from automat import Automat
from shotgun import Shotgun
from enemy_rat import EnemyRat
from bullet_case import BulletCase
from enemy_sniper import EnemySniper


class Room:
    def __init__(self, player, images, x, y, w, h, doors, is_arena=False):
        rooms.append(self)
        self.is_arena = is_arena
        self.spawn_time = 2
        self.player = player
        self.doors = []
        self.height = images["wall_block_hor"].get_rect()[H]
        self.width = images["wall_block_ver"].get_rect()[W]
        self.rect_f = [x, y, w * METR + self.width * 2, h * METR + self.height * 2]
        self.tag = "room"
        self.battle = False
        self.used = False
        self.walls = {"up": [], "down": [], "left": [], "right": []}
        self.enemies = []
        self.types_enemyes = {1: "enemy_rat", 2: "enemy_sniper"}
        if not DELETE_ENEMIES:
            self.max_enemies_one_room = 1
            self.min_enemies_one_room = 1
            self.min_enemies_one_wave = 1
            self.max_enemies_one_wave = 1
        else:
            self.max_enemies_one_room = 0
            self.min_enemies_one_room = 0
            self.min_enemies_one_wave = 0
            self.max_enemies_one_wave = 0
        self.count_enemies_one_room = None
        self.count_enemies_one_wave = None
        self.chance_spawn_aid = 60
        self.left = None
        self.colliders = {
            "default": Collider(self, 3 * METR, 3 * METR, self.rect_f[W] - 6 * METR, self.rect_f[H] - 6 * METR, True),
            "check_door": Collider(self, METR * 2, METR * 2, self.rect_f[W] - 4 * METR, self.rect_f[H] - 4 * METR,
                                   True)}
        for i in range(len(doors)):
            self.walls[doors[i][0]].append(doors[i])
        for i in self.walls:
            if i == "up":
                self.walls[i] = Wall(self, "up", images, 0, 0, w, self.walls[i])
            elif i == "down":
                self.walls[i] = Wall(self, "down", images, 0, self.rect_f[H] - self.height, w,
                                     self.walls[i])
            elif i == "left":
                self.walls[i] = Wall(self, "vertical", images, 0, self.height, h, self.walls[i])
            else:
                self.walls[i] = Wall(self, "vertical", images, self.rect_f[W] - self.width, self.height, h,
                                     self.walls[i])
        self.surface = Surface(self, images, self.width, self.height, w, h)

    def move_camera(self, x, y):
        self.rect_f[X] -= x
        self.rect_f[Y] -= y
        self.surface.move_camera(x, y)
        for i in self.walls:
            self.walls[i].move_camera(x, y)

    def draw(self, screen):
        self.surface.draw(screen)
        for i in self.walls:
            self.walls[i].draw(screen)

    def unit_collided(self, collider, unit):
        pass

    def spawn_enemies_instead(self):
        for i in spawns:
            rect = i.rect
            i.kill()
            self.convert_name_in_enemy(self.enemies[0], rect[X], rect[Y])
            del self.enemies[0]

    def convert_name_in_enemy(self, name, x, y):
        if name == "enemy_rat":
            EnemyRat(self.player, x, y)
        elif name == "enemy_sniper":
            EnemySniper(self.player, x, y)

    def random_spawn(self):
        return [randint(int(self.colliders["default"].rect_f[X]),
                        int(self.colliders["default"].rect[X]) +
                        int(self.colliders["default"].rect[W])),
                randint(int(self.colliders["default"].rect[Y]),
                        int(self.colliders["default"].rect[Y]) +
                        int(self.colliders["default"].rect[H]))]

    def spawn_one(self):
        spawn_zone = Sprite(spawns, object_sprites, background)
        spawn_zone.image = TEXTURES_DEFAULT["spawn_delay"]
        spawn_zone.rect_f = spawn_zone.image.get_rect().move(*self.random_spawn())
        spawn_zone.rect = pygame.Rect(spawn_zone.rect_f)
        while len(pygame.sprite.spritecollide(spawn_zone, spawns, False)) > 1:
            spawn_zone.kill()
            spawn_zone = Sprite(spawns, object_sprites, background)
            spawn_zone.image = TEXTURES_DEFAULT["spawn_delay"]
            spawn_zone.rect_f = spawn_zone.image.get_rect().move(*self.random_spawn())
            spawn_zone.rect = pygame.Rect(spawn_zone.rect_f)

    def spawn_consumables(self):
        chance = randint(1, 100)
        if chance <= self.chance_spawn_aid:
            Aid(self.player, *self.random_spawn())
        if not self.battle and arenas.index(self) % 2:
            BulletCase(self.player, *self.random_spawn())

    def spawn(self):
        self.spawn_consumables()
        if not self.battle:
            self.count_enemies_one_room = randint(self.min_enemies_one_room, self.max_enemies_one_room)
            self.left = self.count_enemies_one_room
        self.count_enemies_one_wave = randint(self.min_enemies_one_wave, self.max_enemies_one_wave)
        if self.min_enemies_one_wave <= self.left <= self.max_enemies_one_wave:
            self.count_enemies_one_wave = self.left
        else:
            while not self.min_enemies_one_wave <= self.left - self.count_enemies_one_wave <= self.max_enemies_one_wave:
                self.count_enemies_one_wave = randint(self.min_enemies_one_wave, self.max_enemies_one_wave)
        self.left -= self.count_enemies_one_wave
        for i in range(self.count_enemies_one_wave):
            enemy = randint(1, COUNT_TYPES_ENEMIES)
            self.enemies.append(self.types_enemyes[enemy])
        for i in range(self.count_enemies_one_wave):
            self.spawn_one()
        if not self.battle:
            self.player.set_arena(self)
            self.player.battle = True
            self.battle = True
            for i in self.doors:
                i.block()
        Timer(self.spawn_time, self.spawn_enemies_instead).start()

    def spawn_weapon(self):
        room = transes[GET_FIRST_WEAPON]
        if self.player.passed_rooms == GET_FIRST_WEAPON:
            Shotgun(self.player, room.rect_f[X] + room.rect_f[W] // 2, room.rect_f[Y] + room.rect_f[H] // 2)
        if self.player.passed_rooms == GET_FIRST_WEAPON + COUNT_OF_ARENAS:
            Automat(self.player, room.rect_f[X] + room.rect_f[W] // 2, room.rect_f[Y] + room.rect_f[H] // 2)

    def end_of_battle(self):
        if self.left == 0:
            self.player.passed_rooms += 1
            if self.player.passed_rooms % 4 == 0:
                self.player.difficult += 1
            self.player.battle = False
            for i in self.doors:
                i.unblock()
            for i in arenas:
                i.used = False
                if i != self and i != arenas[(arenas.index(self) + 1) % len(arenas)]:
                    i.block_all_doors()
                if i == arenas[(arenas.index(self) + 1) % len(arenas)]:
                    i.unblock_all_doors()
            self.used = True
            self.battle = False
            self.spawn_weapon()
        else:
            self.spawn()

    def block_all_doors(self):
        for i in self.doors:
            i.block()

    def unblock_all_doors(self):
        for i in self.doors:
            i.unblock()
