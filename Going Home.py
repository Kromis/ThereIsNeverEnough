import os, sys
import pygame
import resources
from Background import Background
from Draw_Comp import Draw_Comp

from pygame.locals import *

class GoingHome:
    def __init__(self):
        pygame.init()
        self.width = resources.width
        self.height = resources.height
        self.screen = pygame.display.set_mode((self.width, self.height))

        for image in resources.all_sprites.values():
            image.convert_alpha()
            
        self.background = Background(self.screen)

        self.gameState = "GAME"
    
    def game_loop(self):
        while resources.main_loop_running:
            if self.gameState == "GAME":
                
                # All mouse inputs go here
                for event in pygame.event.get():
                    if (event.type == pygame.QUIT):
                        resources.main_loop_running = False
                
                self.background.cloud_update()
                self.background.draw()
                Draw_Comp("cannon.png", self.screen, (200, 500)).draw(True, False
)


            pygame.display.update()
        pygame.quit()

if __name__ == "__main__":
    MainWindow = GoingHome()
    MainWindow.game_loop()
