import os
import pygame
from various import *
from sprites import *


class Menu:
    def __init__(self):
        self.start_game = False
        self.max_resolution = self.max_x_size, self.max_y_size = 1920, 1080
        self.middle_resolution = self.middle_x_size, self.middle_y_size = 1600, 900
        self.min_resolution = self.min_x_size, self.min_y_size = 1280, 720
        self.resolution = self.x_size, self.y_size = size
        self.background = pygame.transform.scale(MENU['menu'], self.resolution)
        self.arrow = pygame.transform.scale(CURSOR['arrow'], (self.x_size // 1280 * 50, self.y_size // 720 * 47))
        self.start_sprite = pygame.sprite.Sprite()
        self.options_sprite = pygame.sprite.Sprite()
        self.exit_sprite = pygame.sprite.Sprite()
        self.start_sprite.rect = MENU['start_collider'].get_rect()
        self.options_sprite.rect = MENU['options_collider'].get_rect()
        self.exit_sprite.rect = MENU['exit_collider'].get_rect()
        self.start_sprite.rect.x = self.x_size / self.max_x_size * 687
        self.start_sprite.rect.y = self.y_size / self.max_y_size * 367
        self.options_sprite.rect.x = self.x_size / self.max_x_size * 687
        self.options_sprite.rect.y = self.y_size / self.max_y_size * 500
        self.exit_sprite.rect.x = self.x_size / self.max_x_size * 687
        self.exit_sprite.rect.y = self.y_size / self.max_y_size * 625

    def render(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.arrow = pygame.transform.scale(CURSOR['arrow_tapped'],
                                                        (self.x_size // 1280 * 50, self.y_size // 720 * 47))
                    if mouse_x > self.start_sprite.rect.x and mouse_y > self.start_sprite.rect.y:
                        if mouse_x < self.start_sprite.rect.x + 585 * self.x_size / self.max_x_size \
                                and mouse_y < self.start_sprite.rect.y + 105 * self.y_size / self.max_y_size:
                            self.background = pygame.transform.scale(MENU["start_tapped"], self.resolution)
                            screen.blit(self.background, self.background.get_rect(bottomright=self.resolution))
                            self.start_game = True
                            pygame.display.flip()
                            pygame.time.Clock().tick(FPS)
                            return False
                    if mouse_x > self.options_sprite.rect.x and mouse_y > self.options_sprite.rect.y:
                        if mouse_x < self.options_sprite.rect.x + 585 * self.x_size / self.max_x_size \
                                and mouse_y < self.options_sprite.rect.y + 105 * self.y_size / self.max_y_size:
                            self.background = pygame.transform.scale(MENU["options_tapped"], self.resolution)
                    if mouse_x > self.exit_sprite.rect.x and mouse_y > self.exit_sprite.rect.y:
                        if mouse_x < self.exit_sprite.rect.x + 585 * self.x_size / self.max_x_size \
                                and mouse_y < self.exit_sprite.rect.y + 105 * self.y_size / self.max_y_size:
                            self.background = pygame.transform.scale(MENU["exit_tapped"], self.resolution)
                            screen.blit(self.background, self.background.get_rect(bottomright=self.resolution))
                            pygame.display.flip()
                            pygame.time.Clock().tick(FPS)
                            return False
            if event.type == pygame.MOUSEBUTTONUP:
                self.arrow = pygame.transform.scale(CURSOR['arrow'],
                                                    (self.x_size // 1280 * 50, self.y_size // 720 * 47))
                self.background = pygame.transform.scale(MENU['menu'], self.resolution)
        if pygame.mouse.get_focused():
            screen.blit(self.background, self.background.get_rect(bottomright=self.resolution))
            screen.blit(self.arrow, self.arrow.get_rect(
                bottomright=(mouse_x + self.x_size // 1280 * 50, mouse_y + self.y_size // 720 * 47)))
        pygame.time.Clock().tick(FPS)
        pygame.display.flip()
        return True

pygame.init()
running = True
screen = pygame.display.set_mode(size, pygame.NOFRAME)
pygame.mouse.set_visible(0)
menu = Menu()
while running:
    running = menu.render()

pygame.quit()

if menu.start_game:
    os.system("main.py")

