from Sprite_Manager import Sprite_Sheet
from SoundManager import SoundManager
import Game
import pygame
import Time

width = 1280
height = 720
all_sprites = Sprite_Sheet("Art").load_all()
time = Time.Time()
pygame.init()

screen = pygame.display.set_mode((width, height))
screen_copied = screen.copy()
main_loop_running = True
game_manager = Game.Game()
state = "START"

sound_manager = SoundManager()

