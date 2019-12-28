from player import Player
from room import Room
from global_various import *


def draw_all_sprites():
    for i in motionless:
        i.draw(screen)
    for i in motionful:
        i.draw(screen)


pygame.init()
sur1 = Room("background.png", width // 2 - 200, height // 2 - 200)
sur2 = Room("background.png", width // 2, height // 2)
player = Player()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player.check_pressed()
    player.change_all_pos()
    draw_all_sprites()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()