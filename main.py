from player import Player
from room import Room
from global_various import *
import time


def draw_all_sprites():
    for i in background:
        i.draw(screen)
    for i in motionless:
        i.draw(screen)
    motionful.draw(screen)
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


pygame.init()
player = Player("player_face.png")
sur2 = Room("surface_block.png", TEXTURES, width // 2 - 300, height // 2 - 300, 20, 10)


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
    player.check_pressed()
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