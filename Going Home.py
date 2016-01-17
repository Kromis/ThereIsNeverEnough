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
        self.gameState = "START"
        
    def game_loop(self):
        while resources.main_loop_running:
            # All mouse inputs go here
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    resources.main_loop_running = False

                    if pygame.mouse.get_pressed()[0]:
                        resources.game_manager.click(pygame.mouse.get_pos())
                        ##                        print(str(pygame.mouse.get_pos()[0]) + ", " + str(pygame.mouse.get_pos()[1]))                    

            if self.gameState == "START":
                if pygame.mouse.get_pressed()[0]:
                    self.gameState = "GAME"
                    resources.game_manager.reset()

                start = resources.all_sprites["start.png"]
                resources.screen.blit(start, (0,0))
                pass

            elif self.gameState == "GAME":
                self.background.update()
                self.background.draw()
                #test = Draw_Comp("shield.png", self.screen, (200, 500))
                #test.draw(False, False)

                resources.game_manager.update()

            elif self.gameState == "END":
                if pygame.mouse.get_pressed()[0]:
                    self.gameState = "START"

                gameOver= resources.all_sprites["gameOver.png"]
                resources.screen.blit(gameOver, (0,0))
                pass

            elif self.gameState == "WIN":
                if pygame.mouse.get_pressed()[0]:
                    self.gameState = "START"

                win= resources.all_sprites["win.png"]
                resources.screen.blit(win, (0,0))
                pass

            pygame.display.update()
        pygame.quit()

if __name__ == "__main__":
    MainWindow = GoingHome()
    MainWindow.game_loop()
