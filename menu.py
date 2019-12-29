import pygame, os

running = True
width = 1600
height = 900


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    image.set_colorkey((255, 255, 255))
    return image


class Menu(pygame.sprite.Sprite):
    def __init__(self):
        self.fps = 120
        self.background = pygame.transform.scale(pygame.image.load('data/Menu.jpg'),  (width, height))
        self.arrow = pygame.transform.scale(pygame.image.load('data/arrow.png'),
                                       (100, 94))
        self.arrow_sprite = pygame.sprite.Sprite()
        self.start_sprite = pygame.sprite.Sprite()
        self.options_sprite = pygame.sprite.Sprite()
        self.exit_sprite = pygame.sprite.Sprite()
        self.start_sprite.rect = load_image('start_collider.png').get_rect()
        self.start_sprite.mask = pygame.mask.from_surface(load_image('start_collider.png'))
        self.options_sprite.rect = load_image('options_collider.png').get_rect()
        self.options_sprite.mask = pygame.mask.from_surface(load_image('options_collider.png'))
        self.exit_sprite.rect = load_image('exit_collider.png').get_rect()
        self.exit_sprite.mask = pygame.mask.from_surface(load_image('exit_collider.png'))

    def render(self):
        self.arrow_sprite.rect = self.arrow.get_rect()
        self.arrow_sprite.mask = pygame.mask.from_surface(self.arrow)
        print(self.start_sprite.rect, self.start_sprite.mask)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.arrow = pygame.transform.scale(pygame.image.load('data/arrow_tapped.png'), (100, 94))
                    if pygame.sprite.collide_mask(self.arrow_sprite, self.start_sprite):
                        self.background = pygame.transform.scale(pygame.image.load('data/start_tapped.jpg'),
                                                                 (width, height))
                    elif pygame.sprite.collide_mask(self.arrow_sprite, self.options_sprite):
                        self.background = pygame.transform.scale(pygame.image.load('data/options_tapped.jpg'),
                                                                 (width, height))
                    elif pygame.sprite.collide_mask(self.arrow_sprite, self.exit_sprite):
                        self.background = pygame.transform.scale(pygame.image.load('data/exit_tapped.jpg'),
                                                                 (width, height))
            if event.type == pygame.MOUSEBUTTONUP:
                self.arrow = pygame.transform.scale(pygame.image.load('data/arrow.png'), (100, 94))
                self.background = pygame.transform.scale(pygame.image.load('data/Menu.jpg'),  (width, height))
        if pygame.mouse.get_focused():
            screen.blit(self.background, self.background.get_rect(bottomright=(width, height)))
            screen.blit(self.arrow, self.arrow.get_rect(bottomright=(pygame.mouse.get_pos())))
        pygame.time.Clock().tick(self.fps)
        pygame.display.flip()
        return True


pygame.init()
screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
pygame.mouse.set_visible(0)
menu = Menu()
while running:
    running = menu.render()

pygame.quit()