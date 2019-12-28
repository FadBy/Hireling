import pygame
import os


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    image.set_colorkey((255, 255, 255))
    return image


def draw_all_sprites():
    for i in Surface.all_sprites:
        screen.blit(i.image, i.rect)
    screen.blit(player.image, player.rect)


class Camera(pygame.sprite.Sprite):
    all_sprites = []

    def __init__(self):
        super().__init__()
        self.rect = [0] * 4

    def move_camera(self, x, y):
        self.rect[0] -= x
        self.rect[1] -= y

    def set_rect(self, rect):
        self.rect[2] = rect[2]
        self.rect[3] = rect[3]

    def set_pos(self, coords):
        self.rect[0] = coords[0]
        self.rect[1] = coords[1]

    def add_in_lst(self, obj):
        self.all_sprites.append(obj)


class Surface(Camera):
    def __init__(self, x, y):
        super().__init__()
        self.add_in_lst(self)
        self.set_pos((x, y))
        self.image = load_image("background.png", -1)
        self.set_rect(self.image.get_rect())


class Player(Camera):
    def __init__(self):
        super().__init__()
        self.image = load_image("player.png", -1)
        self.set_pos((width // 2, height // 2))
        self.set_rect(self.image.get_rect())
        self.change_x = 0
        self.change_y = 0
        self.speed_run = 100 // FPS

    def run(self, coord, way):
        if coord == 0:
            self.change_x += self.speed_run * way
        else:
            self.change_y = self.speed_run * way

    def check_pressed(self):
        pressed_btns = pygame.key.get_pressed()
        if pressed_btns[pygame.K_a]:
            self.run(0, -1)
        if pressed_btns[pygame.K_d]:
            self.run(0, 1)
        if pressed_btns[pygame.K_w]:
            self.run(1, -1)
        if pressed_btns[pygame.K_s]:
            self.run(1, 1)

    def change_all_pos(self):
        for i in self.all_sprites:
            i.move_camera(self.change_x, self.change_y)
        self.change_x = 0
        self.change_y = 0






pygame.init()
FPS = 60
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
sur1 = Surface(width // 2 - 200, height // 2 - 200)
sur2 = Surface(width // 2, height // 2)
player = Player()
running = True

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player.check_pressed()
    player.change_all_pos()
    draw_all_sprites()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
