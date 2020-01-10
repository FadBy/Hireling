import os
import pygame
from all_various import *

running = True


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    image.set_colorkey((255, 255, 255))
    return image


class Menu(pygame.sprite.Sprite):
    def __init__(self):
        self.start_game = False
        self.fps = 120
        self.background = pygame.transform.scale(MENU["menu"], (width, height))
        self.arrow = pygame.transform.scale(CURSOR["arrow"],
                                            (width // 1280 * 50, height // 720 * 47))
        self.start_sprite = pygame.sprite.Sprite()
        self.options_sprite = pygame.sprite.Sprite()
        self.exit_sprite = pygame.sprite.Sprite()
        self.start_sprite.rect = MENU["start_collider.png"].get_rect()
        self.start_sprite.rect.x, self.start_sprite.rect.y = width / 1600 * 575, height / 900 * 305
        self.options_sprite.rect = MENU["options_collider"].get_rect()
        self.options_sprite.rect.x, self.options_sprite.rect.y = width / 1600 * 575, height / 900 * 415
        self.exit_sprite.rect = MENU["exit_collider"].get_rect()
        self.exit_sprite.rect.x, self.exit_sprite.rect.y = width / 1600 * 575, height / 900 * 525

    def render(self):
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.arrow = pygame.transform.scale(CURSOR["arrow_tapped"],
                                                        (width // 1280 * 50, height // 720 * 47))
                    if x > self.start_sprite.rect.x and y > self.start_sprite.rect.y:
                        if x < self.start_sprite.rect.x + 595 * width / 1980 \
                                and y < self.start_sprite.rect.y + 120 * height / 1280:
                            self.background = pygame.transform.scale(MENU["start_tapped"],
                                                                     (width, height))
                            screen.blit(self.background, self.background.get_rect(bottomright=(width, height)))
                            self.start_game = True
                            pygame.display.flip()
                            pygame.time.Clock().tick(self.fps)
                            return False
                    if x > self.options_sprite.rect.x and y > self.options_sprite.rect.y:
                        if x < self.options_sprite.rect.x + 595 * width / 1980 \
                                and y < self.options_sprite.rect.y + 115 * height / 1280:
                            self.background = pygame.transform.scale(MENU["options_tapped"],
                                                                     (width, height))
                    if x > self.exit_sprite.rect.x and y > self.exit_sprite.rect.y:
                        if x < self.exit_sprite.rect.x + 595 * width / 1980 \
                                and y < self.exit_sprite.rect.y + 115 * height / 1280:
                            self.background = pygame.transform.scale(MENU["exit_tapped"],
                                                                     (width, height))
                            screen.blit(self.background, self.background.get_rect(bottomright=(width, height)))
                            pygame.display.flip()
                            pygame.time.Clock().tick(self.fps)
                            return False
            if event.type == pygame.MOUSEBUTTONUP:
                self.arrow = pygame.transform.scale(CURSOR["arrow"],
                                                    (width // 1280 * 50, height // 720 * 47))
                self.background = pygame.transform.scale(MENU["menu"], (width, height))
        if pygame.mouse.get_focused():
            screen.blit(self.background, self.background.get_rect(bottomright=(width, height)))
            screen.blit(self.arrow, self.arrow.get_rect(bottomright=(x + width // 1280 * 50, y + height // 720 * 47)))
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

if menu.start_game:
    os.system("main.py")
