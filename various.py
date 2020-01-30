import pygame

collider_group = pygame.sprite.Group()

rooms = []
background = []
motionful = []
middle = []
object_sprites = []
interface_content = []
enemies = pygame.sprite.Group()
decors = []
arenas = []
spawns = pygame.sprite.Group()


size = width, height = 1280, 720
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size, pygame.NOFRAME)

VERTICAL_SPRITE = 0
FULL_CORNER_SPRITE = 1
NOT_FULL_CORNER_SPRITE = 2
WALL_SPRITE = 3

X = 0
Y = 1
W = 2
H = 3

METR = 75
WIDTH_WALL_COLLIDER = 0.75
WALL_SHIFT = 21
WIDTH_UNIT_COLLIDER = 0.2
HEIGHT_UNIT_COLLIDER = 0.5
INDENT_UNIT_COLLIDET = 0.2

FPS = 60

COUNT_OF_ILLUSIONS = 4

COUNT_OF_ENEMIES = 3
