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
                    "corner_down": load_image("textures_default/corner_down.png")
                    }

PLAYER = {"player_back1": load_image('player/player_back1.png'),
          "player_back2": load_image('player/player_back2.png'),
          "player_back201": load_image('player/player_back201.png'),
          "player_back3": load_image('player/player_back3.png'),
          "player_face": load_image("player/player_face.png"),
          "player_left": load_image('player/player_left.png'),
          "player_right": load_image("player/player_right.png")}

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
           "vorog": load_image("bullets/vorogg.png")}
