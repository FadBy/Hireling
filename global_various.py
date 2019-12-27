import pygame
import os


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    image.set_colorkey((255, 255, 255))
    return image


player_group = pygame.sprite.Group()
enemys_group = pygame.sprite.Group()
surface_group = pygame.sprite.Group()
walls_front_group = pygame.sprite.Group()
walls_back_group = pygame.sprite.Group()
walls_side_group = pygame.sprite.Group()

layers = [surface_group, walls_back_group, enemys_group, player_group, walls_front_group]

FPS = 60

size = width, height = 800, 600
