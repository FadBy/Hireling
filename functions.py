import os
import pygame
from various import *


def load_image(name, colorkey=(255, 255, 255)):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    image.set_colorkey(colorkey)
    return image


def sort_groups():
    rooms.sort(key=lambda x: x.rect_f[0], reverse=True)
