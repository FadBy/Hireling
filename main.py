from map import *
from functions import *


def check_colliders():
    for i in motionful:
        for j in i.colliders:
            colliders = pygame.sprite.spritecollide(i.colliders[j], collider_group, False)
            for u in colliders:
                if u.owner != i:
                    if u.trigger:
                        u.unit_collided(i.colliders[j])
                    elif not i.colliders[j].trigger:
                        u.default_collided(i.colliders[j])
                    if i.colliders[j].trigger:
                        i.colliders[j].unit_collided(u)


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
    if len(enemies) == 0 and player.battle and len(spawns) == 0:
        player.battle = False
        doors = player.arena.doors
        for i in doors:
            i.stop_blocking()
    for i in enemies:
        if i.health <= 0:
            i.kill()
        else:
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
                color = (255, 0, 0)
            else:
                color = (255, 255, 255)
            pygame.draw.rect(screen, color, pygame.Rect(*i.rect_f), 5)
    for i in interface_content:
        i.draw(screen)


pygame.init()

TEST_COLLIDER = True
PRINT_FPS = False
ENEMYS_ATTACK = True


player.set_arena(arenas[0])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    tick = clock.tick() / 1000
    for i in motionful:
        i.set_tick(tick)
    pressed = player.check_pressed()
    if pressed != '':
        running = pressed
    for i in motionful:
        i.set_tick(tick)
    change_all_pos()
    check_colliders()
    change_all_pos()
    screen.fill((0, 0, 0))
    if ENEMYS_ATTACK:
        enemy_action()
    draw_all_sprites()
    if player.interface.health <= 0:
        running = False
    if PRINT_FPS:
        print(int(clock.get_fps()))
    pygame.display.flip()
pygame.quit()
