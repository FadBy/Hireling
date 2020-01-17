import pygame
from all_various import *
from sprite import Sprite


class Collider(Sprite):
    def __init__(self, owner, x, y, w, h, trigger=False):
        super().__init__(collider_group)
        self.trigger = trigger
        self.image = pygame.Surface((w, h))
        self.rect_f = [x + owner.rect_f[X], y + owner.rect_f[Y], w, h]
        self.rect = pygame.Rect(self.rect_f)
        self.owner = owner

    def move_camera(self, x, y):
        self.rect_f[X] -= x
        self.rect_f[Y] -= y
        self.rect = pygame.Rect(self.rect_f)

    def move(self, x, y):
        self.rect_f[X] += x
        self.rect_f[Y] += y
        self.rect = pygame.Rect(self.rect_f)

    def default_collide(self, player):
        player = player.collider
        if player.rect_f[X] <= self.rect_f[X] and player.rect_f[Y] >= self.rect_f[Y] and \
                player.rect_f[Y] + player.rect_f[H] <= self.rect_f[Y] + self.rect_f[H]:
            player.owner.change_x = self.rect_f[X] - player.rect_f[X] - player.rect_f[W]
        elif player.rect_f[X] + player.rect_f[W] >= self.rect_f[X] + self.rect_f[W] and \
                player.rect_f[Y] >= self.rect_f[Y] and \
                player.rect_f[Y] + player.rect_f[H] <= self.rect_f[Y] + self.rect_f[H]:
            player.owner.change_x = self.rect_f[X] + self.rect_f[W] - player.rect_f[X]
        elif player.rect_f[Y] <= self.rect_f[Y] and player.rect_f[X] >= self.rect_f[X] and \
                player.rect_f[X] + player.rect_f[W] <= self.rect_f[X] + self.rect_f[W]:
            player.owner.change_y = self.rect_f[Y] - player.rect[Y] - player.rect_f[H]
        elif player.rect_f[Y] + player.rect_f[H] >= self.rect_f[Y] and player.rect_f[
            X] >= \
                self.rect_f[X] and player.rect_f[X] + player.rect_f[W] <= self.rect_f[X] + \
                self.rect_f[W]:
            player.owner.change_y = self.rect_f[Y] + self.rect_f[H] - player.rect_f[Y]
        elif player.rect_f[X] <= self.rect_f[X] and player.rect_f[Y] <= self.rect_f[Y] and player.rect_f[Y] + \
                player.rect_f[H] - self.rect_f[Y] >= player.rect_f[X] + player.rect_f[W] - self.rect_f[X] or \
                player.rect_f[X] <= self.rect_f[X] + self.rect_f[W] and player.rect_f[Y] + player.rect_f[H] >= \
                self.rect_f[Y] + self.rect_f[H] and \
                self.rect_f[Y] + self.rect_f[H] - player.rect_f[Y] >= player.rect_f[W] + player.rect_f[X] \
                - self.rect_f[X]:
            player.owner.change_x = self.rect_f[X] - player.rect_f[X] - player.rect_f[W]
        elif player.rect_f[X] <= self.rect_f[X] and player.rect_f[Y] <= self.rect_f[Y] and player.rect_f[Y] + \
                player.rect_f[H] - self.rect_f[Y] <= player.rect_f[X] + player.rect_f[W] - self.rect_f[X] or \
                player.rect_f[Y] <= self.rect_f[Y] and player.rect_f[X] + player.rect_f[W] >= self.rect_f[X] + \
                self.rect_f[W] and \
                player.rect_f[Y] + player.rect_f[H] - self.rect_f[Y] < self.rect_f[X] + self.rect_f[W] \
                - player.rect_f[X]:
            player.owner.change_y = self.rect_f[Y] - player.rect[Y] - player.rect_f[H]
        elif player.rect_f[Y] <= self.rect_f[Y] and player.rect_f[X] + player.rect_f[W] >= self.rect_f[X] + self.rect_f[
            W] and \
                self.rect_f[Y] - player.rect_f[Y] - player.rect_f[H] <= self.rect_f[X] + self.rect_f[W] - player.rect_f[
            X] or \
                player.rect_f[X] + player.rect_f[W] >= self.rect_f[X] + self.rect_f[W] and player.rect_f[Y] + \
                player.rect_f[H] >= \
                self.rect_f[Y] + self.rect_f[H] and self.rect_f[Y] + self.rect_f[H] - player.rect_f[Y] >= self.rect_f[
            X] + \
                self.rect_f[W] - player.rect_f[X]:
            player.owner.change_x = self.rect_f[X] + self.rect_f[W] - player.rect_f[X]
        elif player.rect_f[X] <= self.rect_f[X] and player.rect_f[Y] + player.rect_f[H] >= self.rect_f[Y] + self.rect_f[
            H] and \
                self.rect_f[Y] + self.rect_f[H] - player.rect_f[Y] <= player.rect_f[W] + player.rect_f[X] - self.rect_f[
            X] or \
                player.rect_f[X] + player.rect_f[W] >= self.rect_f[X] + self.rect_f[W] and player.rect_f[Y] + \
                player.rect_f[H] >= self.rect_f[Y] + self.rect_f[H] and self.rect_f[Y] + self.rect_f[H] - player.rect_f[
            Y] <= \
                self.rect_f[X] + self.rect_f[W] - player.rect_f[X]:
            player.owner.change_y = self.rect_f[Y] + self.rect_f[H] - player.rect_f[Y]
