import random
import resources

class Background:
    def __init__(self):
        self.screen = resources.screen
        
        self.background = resources.all_sprites["background.png"]
        self.ship = resources.all_sprites["ship.png"]
        self.clock = resources.all_sprites["clock.png"]
        self.health = resources.all_sprites["health.png"]
        self.glow = resources.all_sprites["glow.png"]
        self.house = resources.all_sprites["house.png"]
        self.light = resources.all_sprites["light.png"]
        self.moon = resources.all_sprites["moon.png"]
        self.sun = resources.all_sprites["sun.png"]
        self.attack = resources.all_sprites["cannon.png"]
        self.engine = resources.all_sprites["engine.png"]
        self.power = resources.all_sprites["engine.png"]
        self.status_green = resources.all_sprites["statusGreen.png"]
        self.status_red = resources.all_sprites["statusRed.png"]

        self.time = resources.game_manager.time
        
        self.sidebar = [self.clock, self.engine, self.health, self.engine, self.attack]     
        self.cloud_list = self.clouds()

    def clouds(self):
        self.cloud_amount = random.randint(3,8)

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
        
    def cloud_update(self):
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

        for item in range(len(self.sidebar)):
            self.screen.blit(self.sidebar[item], (10, 100*item))

            
            
            if item != 0:
                self.screen.blit(self.status_red, (110, 50 + 100*item))
                self.screen.blit(self.status_green, (110, 50 + 100*item))
