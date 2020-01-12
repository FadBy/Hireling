from player import Player
from room import Room
import time
from all_various import *
from test import *


def draw_all_sprites():

    for i in background:
        i.draw(screen)
    for i in walls:
        i.draw(screen)
    for i in motionful:
        i.draw(screen)
    collusions = []
    for i in motionful:
        element = [i]
        for j in motionless:
            if isinstance(j, pygame.sprite.Group):
                if pygame.sprite.spritecollide(i, j, False):
                    element.append(j)
            else:
                if pygame.sprite.collide_rect(i, j):
                    element.append(j)
        for j in motionful:
            if pygame.sprite.collide_rect(i, j):
                element.append(j)
        collusions.append(element)
    for i in collusions:
        i.sort(key=lambda x: x.rect_f[1] + x.rect_f[3])
        for j in i:
            j.draw(screen)
    if TEST_COLLIDER:
        for i in motionless_collider_group:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(*i.rect_f), 5)
        for i in motionful_collider_group:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(*i.rect_f))


# ticks = pygame.time.get_ticks()
# print(pygame.time.get_ticks() - ticks)
pygame.init()
player = Player()
sur1 = Room(TEXTURES_DEFAULT, width // 2 - 300, height // 2 - 300, 20, 10, [["up", 5]])
sort_groups()
screen = pygame.display.set_mode(size)  # pygame.NOFRAME

TEST_COLLIDER = True
PRINT_FPS = True

running = True
# x = 0
while running:
    # last_frame = time.time()
    # print(last_frame)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player.set_tick(clock.tick() / 1000)
    if player.check_pressed() == 'paused':
        paused = True
        while paused:
            pressed_btns = pygame.key.get_pressed()
            if not pressed_btns[pygame.K_ESCAPE]:
                paused = False
            little_menu = pygame.transform.scale(pygame.image.load('data/Ingame_menu.jpg'), (width, height))
            screen.blit(little_menu, little_menu.get_rect(bottomright=(width, height)))
    player.change_all_pos()
    player.check_colliders()
    player.change_all_pos()
    player.change_x = 0
    player.change_y = 0
    draw_all_sprites()
    pygame.display.flip()
    if PRINT_FPS:
        (print(int(clock.get_fps())))
    # while time.time() < last_frame + 1 / FPS:
    #   pass
    # last_frame = time.time()
    # print(last_frame)
    # x += 1

pygame.quit()