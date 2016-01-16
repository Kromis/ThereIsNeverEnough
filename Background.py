import random
import resources

class Background:
    def __init__(self, screen):
        self.screen = screen
        self.background = resources.all_sprites["background.png"]
        self.ship = resources.all_sprites["ship.png"]
        self.clock = resources.all_sprites["clock.png"]
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
        self.screen.blit(self.clock, (10, 0))
