import pygame



def bipe():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("airplane-beep-sound-effect.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pass