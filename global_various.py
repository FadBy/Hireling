import pygame
import os


def load_image(name, colorkey=(255, 255, 255)):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    image.set_colorkey(colorkey)
    return image


TEXTURES = ["wall_block_ver.png", "full_corner.png", "not_full_corner.png", "wall_block_hor.png"]

rooms = []
background = []
motionless = []
motionful = pygame.sprite.Group()

collider_group = pygame.sprite.Group()

VERTICAL_SPRITE = 0
FULL_CORNER_SPRITE = 1
NOT_FULL_CORNER_SPRITE = 2
WALL_SPRITE = 3

FULL_CORNER = True


METR = 50

FPS = 20
size = width, height = 1280, 720
