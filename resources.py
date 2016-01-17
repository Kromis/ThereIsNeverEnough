from Sprite_Manager import Sprite_Sheet
import Game
import pygame

width = 1280
height = 720
all_sprites = Sprite_Sheet("Art").load_all()

pygame.init()
screen = pygame.display.set_mode((width, height))
main_loop_running = True
game_manager = Game.Game(screen)
