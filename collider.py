import pygame
from all_various import *


class Collider(pygame.sprite.Sprite):
    def __init__(self, owner, x, y, w, h, trigger=False):
        super().__init__()
        if owner in motionless:
            motionless_collider_group.add(self)
        else:
            motionful_collider_group.add(self)
        self.trigger = trigger
        self.image = pygame.Surface((w, h))
        self.rect_f = [x + owner.rect_f[0], y + owner.rect_f[1], w, h]
        self.rect = pygame.Rect(*self.rect_f)
        self.owner = owner

    def move_camera(self, x, y):
        self.rect_f[0] -= x
        self.rect_f[1] -= y
        self.rect = pygame.Rect(self.rect_f)

    def default_collide(self, player):
        if player.rect_f[0] <= self.rect_f[0] and player.rect_f[1] >= self.rect_f[1] and \
                player.rect_f[1] + player.rect_f[3] <= self.rect_f[1] + self.rect_f[3]:
            player.owner.change_x = self.rect_f[0] - player.rect_f[0] - player.rect_f[2]
        elif player.rect_f[0] + player.rect_f[2] >= self.rect_f[0] + self.rect_f[2] and \
                player.rect_f[1] >= self.rect_f[1] and \
                player.rect_f[1] + player.rect_f[3] <= self.rect_f[1] + self.rect_f[3]:
            player.owner.change_x = self.rect_f[0] + self.rect_f[2] - player.rect_f[0]
        elif player.rect_f[1] <= self.rect_f[1] and player.rect_f[0] >= self.rect_f[0] and \
                player.rect_f[0] + player.rect_f[2] <= self.rect_f[0] + self.rect_f[2]:
            player.owner.change_y = self.rect_f[1] - player.rect[1] - player.rect_f[3]
        elif player.rect_f[1] + player.rect_f[3] >= self.rect_f[1] and player.rect_f[
            0] > \
                self.rect_f[0] and player.rect_f[0] + player.rect_f[2] <= self.rect_f[0] + \
                self.rect_f[2]:
            player.owner.change_y = self.rect_f[1] + self.rect_f[3] - player.rect_f[1]
        elif player.rect_f[0] < self.rect_f[0] and player.rect_f[1] < self.rect_f[1] and player.rect_f[1] + \
                player.rect_f[3] - self.rect_f[1] > player.rect_f[0] + player.rect_f[2] - self.rect_f[0] or \
                player.rect_f[0] < self.rect_f[0] + self.rect_f[2] and player.rect_f[1] + player.rect_f[3] > \
                self.rect_f[1] + self.rect_f[3] and \
                self.rect_f[1] + self.rect_f[3] - player.rect_f[1] > player.rect_f[2] + player.rect_f[0] - self.rect_f[
            0]:
            player.owner.change_x = self.rect_f[0] - player.rect_f[0] - player.rect_f[2]
        elif player.rect_f[0] < self.rect_f[0] and player.rect_f[1] < self.rect_f[1] and player.rect_f[1] + \
                player.rect_f[3] - self.rect_f[1] < player.rect_f[0] + player.rect_f[2] - self.rect_f[0] or \
                player.rect_f[1] < self.rect_f[1] and player.rect_f[0] + player.rect_f[2] > self.rect_f[0] + \
                self.rect_f[2] and \
                player.rect_f[1] + player.rect_f[3] - self.rect_f[1] < self.rect_f[0] + self.rect_f[2] - player.rect_f[
            0]:
            player.owner.change_y = self.rect_f[1] - player.rect[1] - player.rect_f[3]
        elif player.rect_f[1] < self.rect_f[1] and player.rect_f[0] + player.rect_f[2] > self.rect_f[0] + self.rect_f[
            2] and \
                self.rect_f[1] - player.rect_f[1] - player.rect_f[3] < self.rect_f[0] + self.rect_f[2] - player.rect_f[
            0] or \
                player.rect_f[0] + player.rect_f[2] > self.rect_f[0] + self.rect_f[2] and player.rect_f[1] + \
                player.rect_f[3] > \
                self.rect_f[1] + self.rect_f[3] and self.rect_f[1] + self.rect_f[3] - player.rect_f[1] > self.rect_f[
            0] + \
                self.rect_f[2] - player.rect_f[0]:
            player.owner.change_x = self.rect_f[0] + self.rect_f[2] - player.rect_f[0]
        elif player.rect_f[0] < self.rect_f[0] and player.rect_f[1] + player.rect_f[3] > self.rect_f[1] + self.rect_f[
            3] and \
                self.rect_f[1] + self.rect_f[3] - player.rect_f[1] < player.rect_f[2] + player.rect_f[0] - self.rect_f[
            0] or \
                player.rect_f[0] + player.rect_f[2] > self.rect_f[0] + self.rect_f[2] and player.rect_f[1] + \
                player.rect_f[3] > self.rect_f[1] + self.rect_f[3] and self.rect_f[1] + self.rect_f[3] - player.rect_f[
            1] < \
                self.rect_f[0] + self.rect_f[2] - player.rect_f[0]:
            player.owner.change_y = self.rect_f[1] + self.rect_f[3] - player.rect_f[1]

