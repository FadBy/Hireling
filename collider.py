import pygame


class Collider(pygame.sprite.Sprite):
    def __init__(self, owner, group, x, y, w, h):
        super().__init__(group)
        self.image = pygame.Surface((w, h))
        self.rect_f = [x, y, w, h]
        self.rect = pygame.Rect(x, y, w, h)
        self.owner = owner

    def change_pos(self, x, y):
        self.rect_f[0] -= x
        self.rect_f[1] -= y
        self.rect = pygame.Rect(self.rect_f)

    def main_collide(self, object_collided):
        if object_collided.tag == "player":
            if object_collided.change_x > 0 and object_collided.change_y == 0:
                object_collided.change_x = self.rect_f[0] - object_collided.rect_f[0] - object_collided.rect_f[2]
            elif object_collided.change_x < 0 and object_collided.change_y == 0:
                object_collided.change_x = self.rect_f[0] + self.rect_f[2] - object_collided.rect_f[0]
            elif object_collided.change_x == 0 and object_collided.change_y > 0:
                object_collided.change_y = self.rect_f[1] - object_collided.rect[1] - object_collided.rect_f[3]
            elif object_collided.change_x == 0 and object_collided.change_y < 0:
                object_collided.change_y = self.rect_f[1] + self.rect_f[3] - object_collided.rect_f[1]
                # asd
            elif object_collided.rect_f[0] < self.rect_f[0] and object_collided.rect_f[1] > self.rect_f[1] and \
                    object_collided.rect_f[1] + object_collided.rect_f[3] < self.rect_f[1] + self.rect_f[3]:
                object_collided.change_x = self.rect_f[0] - object_collided.rect_f[0] - object_collided.rect_f[2]
            elif object_collided.rect_f[0] + object_collided.rect_f[2] > self.rect_f[0] + self.rect_f[2] and \
                    object_collided.rect_f[1] > self.rect_f[1] and \
                    object_collided.rect_f[1] + object_collided.rect_f[3] < self.rect_f[1] + self.rect_f[3]:
                object_collided.change_x = self.rect_f[0] + self.rect_f[2] - object_collided.rect_f[0]
            elif object_collided.rect_f[1] < self.rect_f[1] and object_collided.rect_f[0] > self.rect_f[0] and \
                    object_collided.rect_f[0] < self.rect_f[0] + self.rect_f[2]:
                object_collided.change_y = self.rect_f[1] - object_collided.rect[1] - object_collided.rect_f[3]
            elif object_collided.rect_f[1] + object_collided.rect_f[3] > self.rect_f[1] and object_collided.rect_f[0] > \
                    self.rect_f[0] and object_collided.rect_f[0] + object_collided.rect_f[2] < self.rect_f[0] + self.rect_f[2]:
                object_collided.change_y = self.rect_f[1] + self.rect_f[3] - object_collided.rect_f[1]

