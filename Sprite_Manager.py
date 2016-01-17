import os, sys
import pygame

class Sprite_Sheet:
    def __init__(self, folder):
        self.folder = folder
        folder_exists = os.path.isdir(self.folder)
        if not folder_exists:
            raise SystemExit('Unable to load sprites folder')

    def load_all(self):
        self.all_sprites = {}
        for root, dirs, files in os.walk(self.folder):
           for file_name in files:
               if file_name[-3:] == "png":
                   self.all_sprites[file_name] = pygame.image.load(os.path.join(self.folder, file_name))
        return self.all_sprites
