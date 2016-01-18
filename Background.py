import random
import resources
import pygame

class Background:
    def __init__(self, game_screen):
        self.screen = game_screen
        self.background = resources.all_sprites["background.png"]
        
        self.ship = resources.all_sprites["ship2.png"]
        self.clock = resources.all_sprites["clock.png"]
        self.health = resources.all_sprites["health.png"]
        self.glow = resources.all_sprites["glow.png"]
        self.house = resources.all_sprites["house.png"]
        self.light = resources.all_sprites["light.png"]
        self.moon = resources.all_sprites["moon.png"]
        self.sun = resources.all_sprites["sun.png"]
        self.power = resources.all_sprites["lightbulb.png"]
        self.cannon = resources.all_sprites["cannon.png"]
        self.status_green = resources.all_sprites["statusGreen.png"]
        self.status_red = resources.all_sprites["statusRed.png"]
        self.sidebar_border = resources.all_sprites["status.png"]
        self.hour_hand = resources.all_sprites["clockHour.png"]
        self.min_hand = resources.all_sprites["clockMinute.png"]
        
        self.sky = self.sun
        self.sky_position = (resources.width/3, 0)

        self.progress_border = resources.all_sprites["progress.png"]
        self.progress_green = resources.all_sprites["progressGreen.png"]
        self.progress_red = resources.all_sprites["progressRed.png"]
        self.house = resources.all_sprites["house.png"]
        
        self.font_size = 70
        self.font = pygame.font.Font(pygame.font.match_font('cooperblack'), self.font_size)
        
        self.status_bar_font_size = 30
        self.status_bar_font = pygame.font.Font(pygame.font.match_font('cooperblack'), self.status_bar_font_size)
        self.status_bar_font_size_small = 20
        self.status_bar_font_small = pygame.font.Font(pygame.font.match_font('cooperblack'), self.status_bar_font_size_small)

        
        
        self.sidebar = [self.clock, self.health, self.power, self.cannon]  
        self.cloud_list = self.clouds()

    def clouds(self):
        self.cloud_amount = random.randint(2,4)

        self.cloud_list = []
        self.cloud_images = []

        for sprite, image in resources.all_sprites.items():
            if "cloud" in sprite:
                self.cloud_images.append(sprite)

        for i in range(0, self.cloud_amount):
            # Random width [0]
            # Random height [1]
            # Random speed [2]
            # Random cloud [3]
            self.cloud_list.append([random.randrange(100, 900),random.randrange(0, 300), random.randint(1,2), self.cloud_images[random.randint(0,len(self.cloud_images) - 1)]])

        self.cloud_images.sort()

        return self.cloud_list, self.cloud_images
        
    def update(self):
        if resources.game_manager.day:
            self.sky = self.sun
        else:
            self.sky = self.moon

        self.time_text = str(resources.game_manager.time)

        for i in range(len(self.cloud_list[0])):
            self.cloud_list[0][i][0] -= self.cloud_list[0][i][2]
            if self.cloud_list[0][i][0] + 300 < 0:
                self.cloud_list[0][i][0] = 1280
                self.cloud_list[0][i][1] = random.randrange(0, 300)
                self.cloud_list[0][i][3] = self.cloud_list[1][random.randint(0, len(self.cloud_list[1]) - 1)]            

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        for i in range(0, len(self.cloud_list[0])):
            self.screen.blit(resources.all_sprites[self.cloud_list[0][i][3]], (self.cloud_list[0][i][0], self.cloud_list[0][i][1]))
        self.screen.blit(self.ship, (50, 200))

##        if not resources.game_manager.day:
##            self.screen.blit(self.night, (0,0))

        
        self.draw_glow((self.sky_position[0] - 50, self.sky_position[1] - 50))
        self.screen.blit(self.sky, self.sky_position)

        self.draw_glow((10 - 100, 200 - 100))
        
        self.screen.blit(self.font.render(self.time_text, True, pygame.Color(255, 255, 255)), (120, 0))
        self.screen.blit(self.font.render(resources.game_manager.time.time_suffix, True, pygame.Color(255, 255, 255)), (320, 0))

        for item in range(len(self.sidebar)):
            self.screen.blit(self.sidebar[item], (10, 100*item))
         
        self.draw_clock_hands()
            
        lightbulb_pos = (468, 245)
        self.draw_glow((lightbulb_pos[0] - 100, lightbulb_pos[1] - 100))
        self.screen.blit(self.power, lightbulb_pos)
        
        self.screen.blit(self.status_red, (110, 50 + 100))
        self.screen.blit(self.status_green, (110, 50 + 100), (0, 0, 200*resources.game_manager.shipHp/resources.game_manager.MAX_SHIP_HP, 20))
        self.screen.blit(self.sidebar_border, (110, 50 + 100))
        self.draw_status_bar_text('Health', '{}/{}'.format(int(resources.game_manager.shipHp), resources.game_manager.MAX_SHIP_HP), (110, 10 + 100)) 


        self.screen.blit(self.status_red, (110, 50 + 200))
        self.screen.blit(self.status_green, (110, 50 + 200), (0, 0, 200*resources.game_manager.ship_power/resources.game_manager.MAX_SHIP_POWER, 20))
        self.screen.blit(self.sidebar_border, (110, 50 + 200))        
        self.draw_status_bar_text('Power', '{}/{}'.format(int(resources.game_manager.ship_power), resources.game_manager.MAX_SHIP_POWER), (110, 10 + 200)) 


        self.screen.blit(self.status_red, (110, 50 + 300))
        self.screen.blit(self.status_green, (110, 50 + 300), (0, 0, resources.game_manager.ship_reload*2, 20))
        self.screen.blit(self.sidebar_border, (110, 50 + 300))
        self.draw_status_bar_text('Weapon', '{}/{}'.format(resources.game_manager.ship_reload, 100),(110, 10 + 300)) 

        self.screen.blit(self.progress_red, (50, 680))
        self.screen.blit(self.progress_green, (50, 680), (0, 0, 1150*(resources.game_manager.ship_progress/resources.game_manager.SHIP_MAX_PROGRESS), 20))
        self.screen.blit(self.progress_border, (50, 680))

        self.screen.blit(self.house, (1150, 630))


    def draw_clock_hands(self):
        self.screen.blit(self.hour_hand, (10, 0))
        self.screen.blit(self.min_hand, (10, 0))
        
    def draw_glow(self, position):
        if self.sky == self.sun:
            self.screen.blit(self.glow, position)
            
    def draw_status_bar_text(self, name, value, position):
        self.screen.blit(self.status_bar_font.render(name, True, pygame.Color(255, 255, 255)), position)
        self.screen.blit(self.status_bar_font_small.render(value, True, pygame.Color(255, 255, 255)), (position[0] + 10, position[1] + 37))






