from math import sqrt, tan, pi, atan
import pygame
from various import *
from sprites import *
from sounds import *


def convert_side_in_angle(side):
    if side == "right":
        return 0
    elif side == "up":
        return 90
    elif side == "left":
        return 180
    elif side == "down":
        return 270
    elif side == "right-up":
        return 45
    elif side == "left-up":
        return 135
    elif side == "left-down":
        return 225
    elif side == "right-down":
        return 315


def set_change_coord(angle, speed):
    if angle % 360 == 0:
        xspeed = speed
        yspeed = 0
    elif angle % 360 == 90:
        xspeed = 0
        yspeed = -speed
    elif angle % 360 == 180:
        xspeed = -speed
        yspeed = 0
    elif angle % 360 == 270:
        xspeed = 0
        yspeed = speed
    else:
        xspeed = speed / sqrt(1 + tan(angle * pi / 180) ** 2)
        yspeed = xspeed * abs(tan(angle * pi / 180))
        if 90 < angle < 270:
            xspeed = -xspeed
        if 0 < angle < 180:
            yspeed = -yspeed
    return [xspeed, yspeed]


def calculate_angle(main, second):
    main = [main[X] + main[W] // 2, main[Y] + main[H] // 2]
    second = [second[X] + second[W] // 2, second[Y] + second[H] // 2]
    angle = atan(abs(second[X] - main[X]) / abs(second[Y] - main[Y])) * 180 / pi
    if second[X] > main[X] and second[Y] < main[Y]:
        return 90 - angle
    elif second[X] < main[X] and second[Y] < main[Y]:
        return 90 + angle
    elif second[X] < main[X] and second[Y] > main[Y]:
        return 270 - angle
    else:
        return 270 + angle


def calculate_distance(main, second):
    main = [main[X] + main[W] // 2, main[Y] + main[H] // 2]
    second = [second[X] + second[W] // 2, second[Y] + second[H] // 2]
    return sqrt((main[X] - second[X]) ** 2 + (main[Y] - second[Y]) ** 2)


def ingame_menu_start():
    paused = True
    little_menu = pygame.transform.scale(INGAME_MENU['ingame_menu'], (width // 2, width // 2))
    while paused:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click.play()
                    if mouse_x > width * 3 // 4 - 41 / 128 * width and mouse_y > height * 15 // 16 - 35 / 72 * height:
                        if mouse_x < width * 3 // 4 - 21.5 / 128 * width:
                            if mouse_y < height * 15 // 16 - 29 / 72 * height:
                                paused = False
                                little_menu = pygame.transform.scale(INGAME_MENU['ingame_menu_continue'],
                                                                     (width // 2, width // 2))
                                running = True
                    if mouse_x > width * 3 // 4 - 41 / 128 * width and mouse_y > height * 15 // 16 - 27.5 / 72 * height:
                        if mouse_x < width * 3 // 4 - 21.5 / 128 * width:
                            if mouse_y < height * 15 // 16 - 21.5 / 72 * height:
                                little_menu = pygame.transform.scale(INGAME_MENU['ingame_menu_options'],
                                                                     (width // 2, width // 2))
                    if mouse_x > width * 3 // 4 - 41 / 128 * width and mouse_y > height * 15 // 16 - 20 / 72 * height:
                        if mouse_x < width * 3 // 4 - 21.5 / 128 * width:
                            if mouse_y < height * 15 // 16 - 14 / 72 * height:
                                paused = False
                                little_menu = pygame.transform.scale(INGAME_MENU['ingame_menu_exit'],
                                                                     (width // 2, width // 2))
                                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                little_menu = pygame.transform.scale(INGAME_MENU['ingame_menu'], (width // 2, width // 2))
        screen.blit(little_menu, little_menu.get_rect(bottomright=(width * 3 // 4, height * 15 // 16)))
        pygame.display.flip()
    return running
