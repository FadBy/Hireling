import pygame

collider_group = pygame.sprite.Group()

rooms = []
background = []
motionful = []
middle = []
timers_with = []

size = width, height = 1280, 720
clock = pygame.time.Clock()

VERTICAL_SPRITE = 0
FULL_CORNER_SPRITE = 1
NOT_FULL_CORNER_SPRITE = 2
WALL_SPRITE = 3

X = 0
Y = 1
W = 2
H = 3

FULL_CORNER = True

METR = 75
WIDTH_WALL_COLLIDER = 0.75
WALL_SHIFT = 21
WIDTH_UNIT_COLLIDER = 0.5

FPS = 60

DISTANCE = 30

TIMER_OBJECT = 0
TIMER_TYPE = 1

AGA = 31