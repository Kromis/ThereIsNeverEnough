import os, sys
import pygame
import resources
import Game
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
        self.game = Game.Game()
        self.gameState = "GAME"
    
    def game_loop(self):
        while resources.main_loop_running:
            if self.gameState == "GAME":
                
                # All mouse inputs go here
                for event in pygame.event.get():
                    if (event.type == pygame.QUIT):
                        resources.main_loop_running = False

                    if pygame.mouse.get_pressed()[0]:
                        self.game.click(pygame.mouse.get_pos())
                        print(str(pygame.mouse.get_pos()[0]) + ", " + str(pygame.mouse.get_pos()[1]))                    
                
                self.background.cloud_update()
                self.background.draw()
                test = Draw_Comp("shield.png", self.screen, (200, 500))
                test.draw(False, False)

            pygame.display.update()
        pygame.quit()

if __name__ == "__main__":
    MainWindow = GoingHome()
    MainWindow.game_loop()
