import pygame
pygame.init()
pygame.mixer.music.load('msc.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input('Agora você escuta?')
