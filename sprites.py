import os
import pygame


def load_image(name):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    return image


TEXTURES_DEFAULT = {"wall_block_ver": load_image("textures_default/wall_block_ver.png"),
                    "wall_block_hor": load_image("textures_default/wall_block_hor.png"),
                    "surface_block": load_image("textures_default/surface_block.png"),
                    "door_close_hor": load_image("textures_default/door_close_hor.png"),
                    "door_open_hor": load_image("textures_default/door_open_hor.png"),
                    "door_close_ver": load_image("textures_default/door_close_ver.png"),
                    "door_open_ver": load_image("textures_default/door_open_ver.png"),
                    "corner_up": load_image("textures_default/corner_up.png"),
                    "corner_down": load_image("textures_default/corner_down.png"),
                    "door_blocked_ver": load_image("textures_default/door_blocked_ver.png"),
                    "spawn_delay": load_image("textures_default/spawn_delay.png"),
                    "door_blocked_hor": load_image("textures_default/door_blocked_hor.png")
                    }

PLAYER = {"player_back1": load_image('player/player_back1.png'),
          "player_back2": load_image('player/player_back2.png'),
          "player_back201": load_image('player/player_back201.png'),
          "player_back3": load_image('player/player_back3.png'),
          "player_face": load_image("player/player_face.png"),
          "player_left": load_image('player/player_left.png'),
          "player_right": load_image("player/player_right.png"),
          "health_point": load_image("player/health_points.png"),
          "dividing_line": load_image("player/interface_line.png"),
          "1": load_image("player/1.png"),
          "2": load_image("player/2.png"),
          "3": load_image("player/3.png"),
          "4": load_image("player/4.png"),
          "5": load_image("player/5.png"),
          "6": load_image("player/6.png"),
          "7": load_image("player/7.png"),
          "8": load_image("player/8.png"),
          "9": load_image("player/9.png"),
          "0": load_image("player/0.png")}

CURSOR = {"arrow": load_image("cursor/arrow.png"),
          "arrow_tapped": load_image("cursor/arrow_tapped.png")}

MENU = {"exit_collider": load_image("menu/exit_collider.png"),
        "exit_tapped": load_image("menu/exit_tapped.jpg"),
        "menu": load_image("menu/menu.jpg"),
        "options_collider": load_image("menu/options_collider.png"),
        "options_tapped": load_image("menu/options_tapped.jpg"),
        "start_collider": load_image("menu/start_collider.png"),
        "start_tapped": load_image("menu/start_tapped.jpg")}

INGAME_MENU = {"ingame_menu": load_image("ingame_menu/Ingame_menu.jpg"),
               "ingame_menu_continue": load_image("ingame_menu/Ingame_menu_continue_tapped.jpg"),
               "ingame_menu_options": load_image("ingame_menu/Ingame_menu_options_tapped.jpg"),
               "ingame_menu_exit": load_image("ingame_menu/Ingame_menu_exit_tapped.jpg")}

BULLETS = {"player_bullet": load_image("bullets/player_bullet.png"),
           "vorog": load_image("bullets/vorogg.png"),
           "vorog_rat": load_image("bullets/vorog_rat.png")}

ITEMS = {"aid": load_image('items/aid.png'),
         "bullet_case": load_image('items/bullet_case.png'),
         "shotgun": load_image("items/shotgun.png"),
         "pistol": load_image("items/pistol.png")}