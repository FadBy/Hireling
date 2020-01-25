from various import *
from sprites import *


def ingame_menu_start():
    paused = True
    little_menu = pygame.transform.scale(INGAME_MENU['ingame_menu'], (width // 2, width // 2))
    while paused:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if mouse_x > width * 3 // 4 - 410 and mouse_y > height * 15 // 16 - 350:
                        if mouse_x < width * 3 // 4 - 215 and mouse_y < height * 15 // 16 - 290:
                            paused = False
                            little_menu = pygame.transform.scale(INGAME_MENU['ingame_menu_continue'],
                                                                 (width // 2, width // 2))
                            running = True
                    if mouse_x > width * 3 // 4 - 410 and mouse_y > height * 15 // 16 - 275:
                        if mouse_x < width * 3 // 4 - 215 and mouse_y < height * 15 // 16 - 215:
                            little_menu = pygame.transform.scale(INGAME_MENU['ingame_menu_options'],
                                                                 (width // 2, width // 2))
                    if mouse_x > width * 3 // 4 - 410 and mouse_y > height * 15 // 16 - 199:
                        if mouse_x < width * 3 // 4 - 215 and mouse_y < height * 15 // 16 - 137:
                            paused = False
                            little_menu = pygame.transform.scale(INGAME_MENU['ingame_menu_exit'],
                                                                 (width // 2, width // 2))
                            running = False
            if event.type == pygame.MOUSEBUTTONUP:
                little_menu = pygame.transform.scale(INGAME_MENU['ingame_menu'], (width // 2, width // 2))
        screen.blit(little_menu, little_menu.get_rect(bottomright=(width * 3 // 4, height * 15 // 16)))
        pygame.display.flip()
    return running
