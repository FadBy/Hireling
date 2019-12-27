from player import Player
from surface import Surface
from global_various import *


def draw_all_sprites():
    for i in Surface.all_sprites:
        screen.blit(i.image, i.rect)
    screen.blit(player.image, player.rect)


pygame.init()
sur1 = Surface(width // 2 - 200, height // 2 - 200)
sur2 = Surface(width // 2, height // 2)
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