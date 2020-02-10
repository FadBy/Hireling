from collider import Collider
from sprite import Sprite
from various import *
from sprites import *
from sounds import *


class Door(Sprite):
    def __init__(self, owner, way, images, x, y):
        super().__init__(background, owner, decors, owner.owner.doors)
        self.is_arena = owner.owner.is_arena
        self.owner = owner
        self.player = owner.owner.player
        self.way = way
        self.tag = "door"
        self.blocked = False
        self.was_open = False
        self.layer_collider = 3
        if way == "horisontal":
            self.image_close = images["door_close_hor"]
            self.image_open = images["door_open_hor"]
            self.image_blocked = images["door_blocked_hor"]

            self.image = self.image_close
            self.rect_f = list(self.image_close.get_rect())
            self.rect_f[X], self.rect_f[Y] = x + owner.rect_f[X], y + owner.rect_f[Y]
            self.rect = pygame.Rect(*self.rect_f)
            self.colliders = {"default": Collider(self, 0, self.rect_f[H] - METR, self.rect_f[W],
                                                  METR, trigger=True)}
        else:
            self.image_close = images["door_close_ver"]
            self.image_open = images["door_open_ver"]
            self.image_blocked = images["door_blocked_ver"]
            self.image = self.image_close
            self.rect_f = list(self.image_close.get_rect())
            self.rect_f[X], self.rect_f[Y] = x + owner.rect_f[X], y + owner.rect_f[Y]
            self.rect = pygame.Rect(*self.rect_f)
            self.colliders = {"default": Collider(self, 0, 0, self.rect_f[W], self.rect_f[H], trigger=True)}

    def draw(self, screen):
        super().draw(screen)
        if not self.owner.owner.battle and self.is_arena and self.image == self.image_close and self.was_open and not \
                self.owner.owner.used and \
                pygame.sprite.collide_rect(self.player.colliders["default"], self.owner.owner.colliders["check_door"]):
            detecting.play()
            mixer.music.play(loops=1)
            self.was_open = False
            self.owner.owner.spawn()
            self.image = self.image_blocked
        elif not self.blocked:
            self.image = self.image_close

    def unit_collided(self, collider, unit):
        if not unit.trigger and not self.blocked:
            self.image = self.image_open
            if not self.was_open:
                doors.play()
                self.was_open = True

    def block(self):
        if not self.blocked:
            self.blocked = True
            self.image = self.image_blocked
            if self.way == "horisontal":
                self.colliders["locked"] = Collider(self, 0, self.rect_f[H] - METR, self.rect_f[W], METR)
            else:
                self.colliders["locked"] = Collider(self, 0, 0, self.rect_f[W], self.rect_f[H])

    def unblock(self):
        if self.blocked:
            self.blocked = False
            self.image = self.image_close
            self.colliders["locked"].kill()
            del self.colliders["locked"]
