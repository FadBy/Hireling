from sprite import Sprite
from various import *


class Collider(Sprite):
    def __init__(self, owner, x, y, w, h, trigger=False):
        super().__init__(collider_group)
        self.trigger = trigger
        self.image = pygame.Surface((w, h))
        self.rect_f = [x + owner.rect_f[X], y + owner.rect_f[Y], w, h]
        if not trigger:
            self.layer = owner.layer_collider
        self.past_rect = self.rect_f.copy()
        self.rect = pygame.Rect(self.rect_f)
        self.owner = owner

    def move_camera(self, x, y):
        self.past_rect = self.rect_f.copy()
        super().move_camera(x, y)

    def move(self, x, y):
        self.rect_f[X] += x
        self.rect_f[Y] += y
        self.rect = pygame.Rect(self.rect_f)

    def default_collided(self, player):
        player_rect = player.rect_f
        collider_rect = self.rect_f
        player_past = player.past_rect
        collider_past = self.past_rect
        change_x = 0
        change_y = 0
        if player_past[Y] + player_past[H] <= collider_past[Y] + collider_past[H] and player_past[X] <= \
                collider_past[X]:
            if player_past[Y] + player_past[H] - collider_past[Y] >= player_past[X] + player_past[W] - \
                    collider_past[X]:
                change_x = collider_rect[X] - player_rect[X] - player_rect[W]
            else:
                change_y = collider_rect[Y] - player_rect[Y] - player_rect[H]
        elif player_past[Y] <= collider_past[Y] and player_past[X] \
                >= collider_past[X]:
            if player_past[Y] + player_past[H] - collider_past[Y] >= collider_past[X] + collider_past[W] - \
                    player_past[X]:
                change_x = collider_rect[X] + collider_rect[W] - player_rect[X]
            else:
                change_y = collider_rect[Y] - player_rect[Y] - player_rect[H]
        elif player_past[Y] >= collider_past[Y] and player_past[X] + player_past[W] >= collider_past[X] + \
                player_past[W]:
            if collider_past[X] + collider_past[W] - player_past[X] >= collider_past[Y] + collider_past[H] - \
                    player_past[Y]:
                change_y = collider_rect[Y] + collider_rect[H] - player_rect[Y]
            else:
                change_x = collider_rect[X] + collider_rect[W] - player_rect[X]
        elif player_past[X] + player_past[W] <= collider_past[X] + collider_past[W] and player_past[Y] + \
                player_past[H] >= collider_past[Y] + collider_past[H]:
            if player_past[X] + player_past[W] - collider_past[X] >= collider_past[Y] + collider_past[H] - \
                    player_past[Y]:
                change_y = collider_rect[Y] + collider_rect[H] - player_rect[Y]
            else:
                change_x = collider_rect[X] - player_rect[X] - player_rect[W]

        player.owner.move_by_collider(change_x, change_y)

    def unit_collided(self, unit):
        self.owner.unit_collided(self, unit)
