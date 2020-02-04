from sprite import Sprite
from various import *

class Weapon(Sprite):
    def __init__(self, owner):
        super().__init__(middle, object_sprites)
        self.owner = owner
        self.image = None
        self.rect_f = []

