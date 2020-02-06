from wall import Wall
from surface import Surface
from various import *
from sprites import *
from collider import Collider
from random import randint
from sprite import Sprite
from watchtimer import Timer
from enemy_sniper import EnemySniper
from aid_kit import Aid
from automat import Automat
from shotgun import Shotgun
from enemy_rat import EnemyRat


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
        self.colliders = {
            "default": Collider(self, 3 * METR, 3 * METR, self.rect_f[W] - 6 * METR, self.rect_f[H] - 6 * METR, True),
            "check_door": Collider(self, METR, METR, self.rect_f[W] - 2 * METR, self.rect_f[H] - 2 * METR, True)}
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
            EnemyRat(self.player, rect[X], rect[Y])

    def spawn_one(self):
        spawn_zone = Sprite(spawns, object_sprites, background)
        spawn_zone.image = TEXTURES_DEFAULT["spawn_delay"]
        spawn_zone.rect_f = spawn_zone.image.get_rect().move(randint(int(self.colliders["default"].rect_f[X]),
                                                                     int(self.colliders["default"].rect[X]) +
                                                                     int(self.colliders["default"].rect[W])),
                                                             randint(int(self.colliders["default"].rect[Y]),
                                                                     int(self.colliders["default"].rect[Y]) +
                                                                     int(self.colliders["default"].rect[H])))
        spawn_zone.rect = pygame.Rect(spawn_zone.rect_f)
        while len(pygame.sprite.spritecollide(spawn_zone, spawns, False)) > 1:
            spawn_zone.kill()
            spawn_zone = Sprite(spawns, object_sprites, background)
            spawn_zone.image = TEXTURES_DEFAULT["spawn_delay"]
            spawn_zone.rect_f = spawn_zone.image.get_rect().move(randint(int(self.colliders["default"].rect[X]),
                                                                         int(self.colliders["default"].rect[X]) +
                                                                         int(self.colliders["default"].rect[W])),
                                                                 randint(int(self.colliders["default"].rect[Y]),
                                                                         int(self.colliders["default"].rect[Y]) +
                                                                         int(self.colliders["default"].rect[H])))
            spawn_zone.rect = pygame.Rect(spawn_zone.rect_f)

    def spawn_consumables(self):
        Aid(self.player, 200, 200)
        Automat(self.player, self.rect_f[X] + 10 * METR, self.rect_f[Y] + 5 * METR)
        Shotgun(self.player, self.rect_f[X] + 15 * METR, self.rect_f[Y] + 5 * METR)

    def spawn(self):
        self.spawn_consumables()
        for i in range(COUNT_OF_ENEMIES):
            self.spawn_one()
        self.player.set_arena(self)
        self.player.battle = True
        self.battle = True
        for i in self.doors:
            i.block()
        Timer(self.spawn_time, self.spawn_enemies_instead).start()

    def end_of_battle(self):
        self.player.battle = False
        self.battle = False
        for i in self.doors:
            i.unblock()
        for i in arenas:
            i.used = False
            if i != self and i != arenas[(arenas.index(self) + 1) % len(arenas)]:
                i.block_all_doors()
            if i == arenas[(arenas.index(self) + 1) % len(arenas)]:
                i.unblock_all_doors()
        self.used = True

    def block_all_doors(self):
        for i in self.doors:
            i.block()

    def unblock_all_doors(self):
        for i in self.doors:
            i.unblock()
