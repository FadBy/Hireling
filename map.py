from player import Player
from room import Room
from sprites import *
from various import *

player = Player()
hubroom = Room(TEXTURES_DEFAULT, width // 2 - 8 * METR, height // 2 - 5 * METR, 14, 7, [["up", 7], ["left", 2]])
transhub = Room(TEXTURES_DEFAULT, width // 2 - 3 * METR, height // 2 - 26.5 * METR, 4, 20, [["down", 2], ["up", 2]])
transroom1 = Room(TEXTURES_DEFAULT, width // 2 - 8 * METR, height // 2 - 32 * METR, 14, 4,
                  [["down", 7], ["left", 2], ["right", 2]])
arenaroom1 = Room(TEXTURES_DEFAULT, width // 2 - 29 * METR, height // 2 - 39 * METR, 20, 15, [["right", 9]])
# transroom2 = Room(TEXTURES_DEFAULT, width // 2 - )
# secroom = Room(TEXTURES_DEFAULT, width // 2 - 300 - 9 * METR, height // 2 - 300 - 5.5 * METR, 18, 4, [["down", 11]])
