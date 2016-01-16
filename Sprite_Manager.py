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
                   self.all[file_name] = pygame.image.load(os.path.join(self.folder, file_name))
        return self.all_sprites

##Seems like we probably don't need animations for this class
##class Animate():
##    def __init__(self, sprite_sheet, total_frames, columns, frame_width, frame_height):
##        self.sprite_sheet = sprite_sheet
##        self.frame = 0
##        self.currentFrame = 0
##        self.total_frames = total_frames
##        self.columns = columns
##        self.row = 0
##        self.clock = pygame.time.Clock()
##        self.frame_width = frame_width
##        self.frame_height = frame_height
##
##    def update(self):
##        if self.currentFrame > self.columns:
##            self.row += 1
##            self.currentFrame = -1
##        if self.frame > self.total_frames - 1:
##            self.frame = -1
##            self.row = 0;
##            self.currentFrame = -1
##
##        self.frame += 1
##        self.currentFrame += 1
##        
##        self.clock.tick(64)
##
##    def draw(self, window, x, y):
##        window.blit(self.image, (x, y), ((self.frame % self.columns) * self.frame_width, self.row * self.frame_height, self.frame_width, self.frame_height))
##        
##
