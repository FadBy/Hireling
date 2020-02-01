from sprite import Sprite
from various import *


class Collider(Sprite):
    def __init__(self, owner, x, y, w, h, trigger=False):
        super().__init__(collider_group)
        self.trigger = trigger
        self.image = pygame.Surface((w, h))
        self.rect_f = [x + owner.rect_f[X], y + owner.rect_f[Y], w, h]
        self.rect = pygame.Rect(self.rect_f)
        self.owner = owner

    def move(self, x, y):
        self.rect_f[X] += x
        self.rect_f[Y] += y
        self.rect = pygame.Rect(self.rect_f)

    def default_collided(self, player):
        player_rect = player.rect_f
        collider_rect = self.rect_f
        moving = [player.owner.past_motion_x, player.owner.past_motion_y]
        change_x = 0
        change_y = 0
        if moving[X] > 0 and moving[Y] == 0:
            change_x = collider_rect[X] - player_rect[X] - player_rect[W]
        elif moving[X] < 0 and moving[Y] == 0:
            change_x = collider_rect[X] + collider_rect[W] - player_rect[X]
        elif moving[Y] > 0 and moving[X] == 0:
            change_y = collider_rect[Y] - player_rect[Y] - player_rect[H]
        elif moving[Y] < 0 and moving[X] == 0:
            change_y = collider_rect[Y] + collider_rect[H] - player_rect[Y]
        elif player_rect[Y] + player_rect[H] < collider_rect[Y] + collider_rect[H] and player_rect[X] < \
                collider_rect[
                    X]:
            if player_rect[Y] + player_rect[H] - collider_rect[Y] > player_rect[X] + player_rect[W] - \
                    collider_rect[X]:
                change_x = collider_rect[X] - player_rect[X] - player_rect[W]
            else:
                change_y = collider_rect[Y] - player_rect[Y] - player_rect[H]

        elif player_rect[Y] < collider_rect[Y] and player_rect[X] \
                > collider_rect[X]:
            if player_rect[Y] + player_rect[H] - collider_rect[Y] > collider_rect[X] + collider_rect[W] - \
                    player_rect[X]:
                change_x = collider_rect[X] + collider_rect[W] - player_rect[X]
            else:
                change_y = collider_rect[Y] - player_rect[Y] - player_rect[H]
        elif player_rect[Y] > collider_rect[Y] and player_rect[X] + player_rect[W] > collider_rect[X] + \
                player_rect[W]:
            if collider_rect[X] + collider_rect[W] - player_rect[X] > collider_rect[Y] + collider_rect[H] - \
                    player_rect[Y]:
                change_y = collider_rect[Y] + collider_rect[H] - player_rect[Y]
            else:
                change_x = collider_rect[X] + collider_rect[W] - player_rect[X]
        elif player_rect[X] + player_rect[W] < collider_rect[X] + collider_rect[W] and player_rect[Y] + \
                player_rect[H] > collider_rect[Y] + collider_rect[H]:
            if player_rect[X] + player_rect[W] - collider_rect[X] > collider_rect[Y] + collider_rect[H] - \
                    player_rect[Y]:
                change_y = collider_rect[Y] + collider_rect[H] - player_rect[Y]
            else:
                change_x = collider_rect[X] - player_rect[X] - player_rect[W]
        player.owner.set_change_moving(change_x, change_y)

        # if player.rect_f[X] <= self.rect_f[X] and player.rect_f[Y] >= self.rect_f[Y] and \
        #         player.rect_f[Y] + player.rect_f[H] <= self.rect_f[Y] + self.rect_f[H]:
        #     player.owner.change_x = self.rect_f[X] - player.rect_f[X] - player.rect_f[W]
        # elif player.rect_f[X] + player.rect_f[W] >= self.rect_f[X] + self.rect_f[W] and \
        #         player.rect_f[Y] >= self.rect_f[Y] and \
        #         player.rect_f[Y] + player.rect_f[H] <= self.rect_f[Y] + self.rect_f[H]:
        #     player.owner.change_x = self.rect_f[X] + self.rect_f[W] - player.rect_f[X]
        # elif player.rect_f[Y] <= self.rect_f[Y] and player.rect_f[X] >= self.rect_f[X] and \
        #         player.rect_f[X] + player.rect_f[W] <= self.rect_f[X] + self.rect_f[W]:
        #     player.owner.change_y = self.rect_f[Y] - player.rect[Y] - player.rect_f[H]
        # elif player.rect_f[Y] + player.rect_f[H] >= self.rect_f[Y] and player.rect_f[
        #     X] >= \
        #         self.rect_f[X] and player.rect_f[X] + player.rect_f[W] <= self.rect_f[X] + \
        #         self.rect_f[W]:
        #     player.owner.change_y = self.rect_f[Y] + self.rect_f[H] - player.rect_f[Y]
        # elif player.rect_f[X] <= self.rect_f[X] and player.rect_f[Y] <= self.rect_f[Y] and player.rect_f[Y] + \
        #         player.rect_f[H] - self.rect_f[Y] >= player.rect_f[X] + player.rect_f[W] - self.rect_f[X] or \
        #         player.rect_f[X] <= self.rect_f[X] + self.rect_f[W] and player.rect_f[Y] + player.rect_f[H] >= \
        #         self.rect_f[Y] + self.rect_f[H] and \
        #         self.rect_f[Y] + self.rect_f[H] - player.rect_f[Y] >= player.rect_f[W] + player.rect_f[X] \
        #         - self.rect_f[X]:
        #     player.owner.change_x = self.rect_f[X] - player.rect_f[X] - player.rect_f[W]
        # elif player.rect_f[X] <= self.rect_f[X] and player.rect_f[Y] <= self.rect_f[Y] and player.rect_f[Y] + \
        #         player.rect_f[H] - self.rect_f[Y] <= player.rect_f[X] + player.rect_f[W] - self.rect_f[X] or \
        #         player.rect_f[Y] <= self.rect_f[Y] and player.rect_f[X] + player.rect_f[W] >= self.rect_f[X] + \
        #         self.rect_f[W] and \
        #         player.rect_f[Y] + player.rect_f[H] - self.rect_f[Y] < self.rect_f[X] + self.rect_f[W] \
        #         - player.rect_f[X]:
        #     player.owner.change_y = self.rect_f[Y] - player.rect[Y] - player.rect_f[H]
        # elif player.rect_f[Y] <= self.rect_f[Y] and player.rect_f[X] + player.rect_f[W] >= self.rect_f[X] + self.rect_f[
        #     W] and \
        #         self.rect_f[Y] - player.rect_f[Y] - player.rect_f[H] <= self.rect_f[X] + self.rect_f[W] - player.rect_f[
        #     X] or \
        #         player.rect_f[X] + player.rect_f[W] >= self.rect_f[X] + self.rect_f[W] and player.rect_f[Y] + \
        #         player.rect_f[H] >= \
        #         self.rect_f[Y] + self.rect_f[H] and self.rect_f[Y] + self.rect_f[H] - player.rect_f[Y] >= self.rect_f[
        #     X] + \
        #         self.rect_f[W] - player.rect_f[X]:
        #     player.owner.change_x = self.rect_f[X] + self.rect_f[W] - player.rect_f[X]
        # elif player.rect_f[X] <= self.rect_f[X] and player.rect_f[Y] + player.rect_f[H] >= self.rect_f[Y] + self.rect_f[
        #     H] and \
        #         self.rect_f[Y] + self.rect_f[H] - player.rect_f[Y] <= player.rect_f[W] + player.rect_f[X] - self.rect_f[
        #     X] or \
        #         player.rect_f[X] + player.rect_f[W] >= self.rect_f[X] + self.rect_f[W] and player.rect_f[Y] + \
        #         player.rect_f[H] >= self.rect_f[Y] + self.rect_f[H] and self.rect_f[Y] + self.rect_f[H] - player.rect_f[
        #     Y] <= \
        #         self.rect_f[X] + self.rect_f[W] - player.rect_f[X]:
        #     player.owner.change_y = self.rect_f[Y] + self.rect_f[H] - player.rect_f[Y]

    def unit_collided(self, unit):
        self.owner.unit_collided(self, unit)
