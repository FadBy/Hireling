from collider import Collider
from sprite import Sprite
from various import *
from sprites import *


class Door(Sprite):
    def __init__(self, owner, way, images, x, y):
        super().__init__(background, owner, decors, owner.owner.doors)
        self.is_arena = owner.owner.is_arena
        self.owner = owner
        self.player = owner.owner.player
        self.way = way
        self.open = False
        self.tag = "door"
        self.was_open = False
        self.battle = False
        if way == "horisontal":
            self.image_close = images["door_close_hor"]
            self.image_open = images["door_open_hor"]
            self.image_blocked = images["door_blocked_ver"]
            self.image = self.image_close
            self.rect_f = list(self.image_close.get_rect())
            self.rect_f[X], self.rect_f[Y] = x + owner.rect_f[X], y + owner.rect_f[Y]
            self.rect = pygame.Rect(*self.rect_f)
            self.colliders = {"default": Collider(self, 0, 0, self.rect_f[W], self.rect_f[H],
                                                  trigger=True)}
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
        if not self.battle and self.is_arena and self.image == self.image_close and self.was_open and \
                pygame.sprite.collide_rect(self.player.colliders["default"], self.owner.owner.colliders["check_door"]):
            self.player.set_arena(self.owner.owner)
            self.player.battle = True
            self.battle = True
            self.image = self.image_blocked
            self.colliders["locked"] = Collider(self, 0, 0, self.rect_f[W], self.rect_f[H])
            self.owner.owner.spawn()
        elif not self.battle:
            self.image = self.image_close

    def unit_collided(self, collider, unit):
        if not unit.trigger and not self.battle:
            self.image = self.image_open
            if not self.was_open:
                self.was_open = True

    def stop_blocking(self):
        self.battle = False
        self.was_open = False
        self.colliders["locked"].kill()
        del self.colliders["locked"]
