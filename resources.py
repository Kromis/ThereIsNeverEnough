from Sprite_Manager import Sprite_Sheet
import Game

main_loop_running = True
width = 1280
height = 720
game_manager = Game.Game()
all_sprites = Sprite_Sheet("Art").load_all()
