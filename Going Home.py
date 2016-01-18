import os, sys
import pygame
import resources
from Draw_Comp import Draw_Comp
from Game import *

from pygame.locals import *

class GoingHome:
    def __init__(self):
        self.width = resources.width
        self.height = resources.height
        #self.clock = pygame.Clock(64)

        for image in resources.all_sprites.values():
            image.convert_alpha()
        
    def game_loop(self):
        clickRect = pygame.Rect(400, 250, 400, 400)
        while resources.main_loop_running:
            mouse_pressed = False
            
            # All mouse inputs go here
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    resources.main_loop_running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pressed = True
                    resources.game_manager.click(pygame.mouse.get_pos())
                    ##                        print(str(pygame.mouse.get_pos()[0]) + ", " + str(pygame.mouse.get_pos()[1]))                    

            if resources.state == "START":
                if mouse_pressed and clickRect.collidepoint(pygame.mouse.get_pos()):
                    resources.state = "GAME"
                    resources.game_manager.reset()

                start = resources.all_sprites["start.png"]
                resources.screen.blit(start, (0,0))
                pass

            elif resources.state == "GAME":
                #test = Draw_Comp("shield.png", self.screen, (200, 500))
                #test.draw(False, False)
                resources.game_manager.update()

            elif resources.state == "LOSE":
                if mouse_pressed and clickRect.collidepoint(pygame.mouse.get_pos()):
                    resources.state = "START"

                gameOver = resources.all_sprites["gameOver.png"]
                resources.screen.blit(gameOver, (0,0))
                pass

            elif resources.state == "WIN":
                if mouse_pressed and clickRect.collidepoint(pygame.mouse.get_pos()):
                    resources.state = "START"

                win = resources.all_sprites["win.png"]
                resources.screen.blit(win, (0,0))
                pass

            pygame.display.update()
        pygame.quit()

if __name__ == "__main__":
    MainWindow = GoingHome()
    MainWindow.game_loop()
