from map import *
from random import randint
from enemy_sniper import EnemySniper


def spawn():
    enemy = EnemySniper(randint(arenaroom1.spawn_area[X], arenaroom1.spawn_area[X] + arenaroom1.spawn_area[W]),
                        randint(arenaroom1.spawn_area[Y], arenaroom1.spawn_area[Y] + arenaroom1.spawn_area[H]))


def check_colliders():
    for i in motionful:
        for j in i.colliders:
            colliders = pygame.sprite.spritecollide(j, collider_group, False)
            for u in colliders:
                if u.owner != i:
                    if u.trigger:
                        u.owner.unit_collided(j)
                    elif not j.trigger:
                        u.default_collide(j)
                    if j.trigger:
                        i.unit_collided(u)


def change_all_pos():
    for i in rooms:
        i.move_camera(player.change_x, player.change_y)
    for i in collider_group:
        if i.owner.tag != "player":
            i.move_camera(player.change_x, player.change_y)
    for i in object_sprites:
        i.move_camera(player.change_x, player.change_y)
    for i in motionful:
        if i != player:
            i.move_camera(player.change_x, player.change_y)
            i.move()
    player.change_x = 0
    player.change_y = 0


def enemy_action():
    for i in enemies:
        i.attack()


def draw_all_sprites():
    for i in background:
        i.draw(screen)
    middle.sort(key=lambda x: x.rect[Y] + x.rect[H])
    for i in middle:
        i.draw(screen)
    if TEST_COLLIDER:
        for i in collider_group:
            if i.trigger:
                color = (0, 255, 0)
            else:
                color = (255, 255, 255)
            pygame.draw.rect(screen, color, pygame.Rect(*i.rect_f), 5)
    for i in interface_content:
        i.draw(screen)


pygame.init()

spawn()

TEST_COLLIDER = True
PRINT_FPS = False

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    tick = clock.tick() / 1000
    pressed = player.check_pressed()
    screen.fill((0, 0, 0))
    if pressed != '':
        running = pressed
    for i in motionful:
        i.set_tick(tick)
    change_all_pos()
    check_colliders()
    change_all_pos()
    enemy_action()
    draw_all_sprites()
    if player.health <= 0:
        running = False
    if PRINT_FPS:
        print(int(clock.get_fps()))
    pygame.display.flip()
pygame.quit()
