import os, sys
import pygame
import resources

from pygame.locals import *

class GoingHome:
    def __init__(self):
        pygame.init()
        self.width = resources.width
        self.height = resources.height
        self.screen = pygame.display.set_mode((self.width, self.height))
        
    def game_loop(self):
        while resources.main_loop_running:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    resources.main_loop_running = False
                    
        pygame.quit()

if __name__ == "__main__":
    MainWindow = GoingHome()
    MainWindow.game_loop()
