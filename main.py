from map import *
from enemy import Enemy


def sort_groups():
    rooms.sort(key=lambda x: x.rect_f[0], reverse=True)


def check_colliders():
    for i in motionful:
        colliders = pygame.sprite.spritecollide(i.collider, collider_group, False)
        if colliders:
            for j in colliders:
                if j.owner != i:
                    if j.trigger:
                        j.owner.unit_collided(i)
                    else:
                        j.default_collide(i)
                    if i.collider.trigger:
                        i.unit_collided(j.owner)


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


def draw_all_sprites():
    for i in background:
        i.draw(screen)
    middle.sort(key=lambda x: x.rect[Y] + x.rect[H])
    for i in middle:
        i.draw(screen)
    if TEST_COLLIDER:
        for i in collider_group:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(*i.rect_f), 5)


def cancel_player_change():
    player.change_x = 0
    player.change_y = 0


pygame.init()

enemies = [Enemy('vorog', random.randint(-500, 1000), random.randint(-500, 1000))]

sort_groups()

screen = pygame.display.set_mode(size, pygame.NOFRAME)

TEST_COLLIDER = False
PRINT_FPS = False

running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    tick = clock.tick() / 1000
    player.check_pressed()
    for i in motionful:
        i.set_tick(tick)
    change_all_pos()
    check_colliders()
    change_all_pos()
    draw_all_sprites()
    hp = player.health_change(enemies[0].attack)
    enemies[0].attack = 0
    # print(hp)
    if not player.alive:
        running = False
    if PRINT_FPS:
        print(int(clock.get_fps()))
    pygame.display.flip()

pygame.quit()
