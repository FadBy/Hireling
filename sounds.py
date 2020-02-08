import os
import pygame


def load_sound(name):
    fullname = os.path.join('data', name)
    sound = pygame.mixer.Sound(fullname)
    return sound


pygame.init()

os.getcwd()
detecting = load_sound('soundtrack\detecting.wav')
detecting.play()
opening = load_sound('soundtrack/doors.wav')
shooting = load_sound('soundtrack/pistol_machinegun.wav')
shotgun_shooting = load_sound('soundtrack/shotgun.wav')
splash = load_sound('soundtrack/splash.mp3')
steps = load_sound('soundtrack/steps.wav')
strike = load_sound('soundtrack/strike.wav')

soundtrack = pygame.mixer.music.load(os.path.join('data', 'soundtrack/Ugh.wav'))
pygame.mixer.music.set_volume(0.4)