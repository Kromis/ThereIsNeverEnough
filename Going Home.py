import os, sys
import pygame
import resources
from Background import Background
from Draw_Comp import Draw_Comp
from Game import *

from pygame.locals import *

class GoingHome:
    def __init__(self):
        self.width = resources.width
        self.height = resources.height

        for image in resources.all_sprites.values():
            image.convert_alpha()
            
        self.background = Background()
        self.gameState = "GAME"
        
    def game_loop(self):
        while resources.main_loop_running:
            if self.gameState == "GAME":
                
                # All mouse inputs go here
                for event in pygame.event.get():
                    if (event.type == pygame.QUIT):
                        resources.main_loop_running = False

                    if pygame.mouse.get_pressed()[0]:
                        resources.game_manager.click(pygame.mouse.get_pos())
##                        print(str(pygame.mouse.get_pos()[0]) + ", " + str(pygame.mouse.get_pos()[1]))                    
                
                self.background.update()
                self.background.draw()
                #test = Draw_Comp("shield.png", self.screen, (200, 500))
                #test.draw(False, False)

                resources.game_manager.update()

            pygame.display.update()
        pygame.quit()

if __name__ == "__main__":
    MainWindow = GoingHome()
    MainWindow.game_loop()
