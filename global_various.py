import pygame
import os


def load_image(name, colorkey=(255, 255, 255)):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    image.set_colorkey(colorkey)
    return image

def sort_groups():
    rooms.sort(key=lambda x: x.rect_f[0], reverse=True)

TEXTURES = ["wall_block_ver.png", "full_corner.png", "not_full_corner.png", "wall_block_hor.png"]

rooms = []
background = []
motionless = []
walls = []
motionful = pygame.sprite.Group()

motionless_collider_group = pygame.sprite.Group()
motionful_collider_group = pygame.sprite.Group()

VERTICAL_SPRITE = 0
FULL_CORNER_SPRITE = 1
NOT_FULL_CORNER_SPRITE = 2
WALL_SPRITE = 3

FULL_CORNER = True

test_collider = False

METR = 50

FPS = 20
size = width, height = 1280, 720
