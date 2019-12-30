from player import Player
from room import Room
from global_various import *


def draw_all_sprites():
    for i in motionless:
        i.draw(screen)
    for i in motionful:
        i.draw(screen)

pygame.init()
player = Player("player_face.png")
sur2 = Room("background_without_height.png", width // 2 - 300, height // 2 - 300)

screen = pygame.display.set_mode(size)  # pygame.NOFRAME
clock = pygame.time.Clock()
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player.check_pressed()
    player.change_all_pos()
    player.check_colliders()
    player.change_all_pos()
    player.change_x = 0
    player.change_y = 0
    draw_all_sprites()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()