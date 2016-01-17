import pygame
import os

class SoundManager:

    def __init__(self):
        self.all_sounds = {}

        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
        self.music = pygame.mixer.music.load('Sound/jammingHome.wav')
        pygame.mixer.music.play(-1)
        
        for file in os.listdir('Sound'):
            if file.endswith(('.ogg', 'wav')):
                #print(file)
                new_sound = pygame.mixer.Sound('Sound/' + file)
                new_sound.set_volume(0.5)
                self.all_sounds[file] = new_sound

    def playCurrentMusic(self):
        pygame.mixer.music.play(-1)

    def playSound(self, filepath):
        self.all_sounds[filepath].play()
