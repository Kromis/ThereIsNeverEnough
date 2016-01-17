import pygame
import os

class SoundManager:

    def __init__(self):
        self.music = None
        self.all_sounds = {}

        #self.syobon = pygame.mixer.music.load("Sound/cannon.wav")
        # Loop music
        #pygame.mixer.music.play(-1)

        for file in os.listdir('Sound'):
            if file.endswith(('.ogg', 'wav')):
                print(file)
                new_sound = pygame.mixer.Sound('Sound/' + file)
                new_sound.set_volume(0.5)
                self.all_sounds[file] = new_sound

    def playCurrentMusic(self):
        pygame.mixer.music.play(-1)

    def playSound(self, filepath):
        self.all_sounds[filepath].play()
