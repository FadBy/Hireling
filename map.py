from player import *
from room import *

class Map:
    def __init__(self):
        self.rect_f = None


player = Player()
mainroom = Room(TEXTURES_DEFAULT, width // 2 - 300, height // 2 - 300, 14, 7, [["left", 5]])
# secroom = Room(TEXTURES_DEFAULT, width // 2 - 300 - 9 * METR, height // 2 - 300 - 5.5 * METR, 18, 4, [["down", 11]])
