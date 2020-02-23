from player import Player
from room import Room
from sprites import *
from various import *


def download_map():
    player.death()
    Room(player, TEXTURES_DEFAULT, width // 2 - 8 * METR, height // 2 - 5 * METR, SIZE_HUB[X], SIZE_HUB[Y],
         [["up", 7], ["left", 2]])
    Room(player, TEXTURES_DEFAULT, width // 2 - 3 * METR, height // 2 - 26.5 * METR, SIZE_TRANSHUB[X],
         SIZE_TRANSHUB[Y],
         [["down", 2], ["up", 2]])
    transes.append(
        Room(player, TEXTURES_DEFAULT, width // 2 - 8 * METR, height // 2 - 32 * METR, SIZE_TRANS[X], SIZE_TRANS[Y],
             [["down", 7], ["left", 2], ["right", 2]]))
    transes.append(
        Room(player, TEXTURES_DEFAULT, width // 2 - 19 * METR, height // 2 - 54.5 * METR, SIZE_TRANS[Y], SIZE_TRANS[X],
             [["down", 2], ["up", 2]]))
    transes.append(
        Room(player, TEXTURES_DEFAULT, width // 2 - 8 * METR, height // 2 - 65 * METR, SIZE_TRANS[X], SIZE_TRANS[Y],
             [["right", 2], ["left", 2]]))
    transes.append(
        Room(player, TEXTURES_DEFAULT, width // 2 + 17 * METR, height // 2 - 54.5 * METR, SIZE_TRANS[Y], SIZE_TRANS[X],
             [["up", 2], ["down", 2]]))
    arenas.append(
        Room(player, TEXTURES_DEFAULT, width // 2 - 29 * METR, height // 2 - 39 * METR, SIZE_ROOM[X], SIZE_ROOM[Y],
             [["right", 9], ["up", 12]],
             True))
    arenas.append(
        Room(player, TEXTURES_DEFAULT, width // 2 - 29 * METR, height // 2 - 72 * METR, SIZE_ROOM[X], SIZE_ROOM[Y],
             [["down", 12], ["right", 9]], True))
    arenas.append(
        Room(player, TEXTURES_DEFAULT, width // 2 + 7 * METR, height // 2 - 72 * METR, SIZE_ROOM[X], SIZE_ROOM[Y],
             [["left", 9], ["down", 12]], True))
    arenas.append(
        Room(player, TEXTURES_DEFAULT, width // 2 + 7 * METR, height // 2 - 39 * METR, SIZE_ROOM[X], SIZE_ROOM[Y],
             [["left", 9], ["up", 12]], True))


def delete_all_lsts():
    collider_group.empty()
    rooms.clear()
    background.clear()
    motionful.clear()
    middle.clear()
    object_sprites.clear()
    interface_content.clear()
    enemies.empty()
    decors.clear()
    arenas.clear()
    transes.clear()
    spawns.empty()
    animations.clear()

player = Player()
