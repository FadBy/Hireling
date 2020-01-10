from player import Player
from room import Room
from global_various import *
import time


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
            if pygame.sprite.spritecollide(i, j, False):
                element.append(j)
        for j in motionful:
            if pygame.sprite.collide_rect(i, j):
                element.append(j)
        collusions.append(element)
    for i in collusions:
        i.sort(key=lambda x: x.rect_f[1])
        for j in i:
            j.draw(screen)
    if test_collider:
        for i in motionless_collider_group:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(*i.rect_f), 5)
        for i in motionful_collider_group:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(*i.rect_f))


pygame.init()

player = Player("player_face.png")
sur1 = Room("surface_block.png", TEXTURES, width // 2 - 300, height // 2 - 300, 20, 10)
sur2 = Room("surface_block.png", TEXTURES, width // 2 - 825, height // 2 - 200, 10, 10)
sort_groups()
screen = pygame.display.set_mode(size)  # pygame.NOFRAME
clock = pygame.time.Clock()
running = True
x = 0
while running:
    last_frame = time.time()
    print(last_frame)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if player.check_pressed() == 'paused':
        paused = True
        while paused:
            pressed_btns = pygame.key.get_pressed()
            if not pressed_btns[pygame.K_ESCAPE]:
                paused = False
            little_menu = pygame.transform.scale(pygame.image.load('data/Ingame_menu.jpg'), (width, height))
            screen.blit(little_menu, little_menu.get_rect(bottomright=(width, height)))
            pygame.display.flip()
    player.change_all_pos()
    player.check_colliders()
    player.change_all_pos()
    player.change_x = 0
    player.change_y = 0
    draw_all_sprites()
    pygame.display.flip()
    while time.time() < last_frame + 1 / FPS:
        pass
    last_frame = time.time()
    print(last_frame)
    x += 1

pygame.quit()