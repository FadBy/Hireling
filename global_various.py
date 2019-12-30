import pygame
import os


def load_image(name, colorkey=(255, 255, 255)):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    image.set_colorkey(colorkey)
    return image


player_group = pygame.sprite.Group()
enemys_group = pygame.sprite.Group()
surface_group = pygame.sprite.Group()
walls_hor_group = pygame.sprite.Group()
walls_ver_group = pygame.sprite.Group()

wall_collider_group = pygame.sprite.Group()

buttons = pygame.sprite.Group()

motionless = [surface_group, walls_hor_group, walls_ver_group]
motionful = [enemys_group, player_group]

FPS = 60
size = width, height = 800, 600
