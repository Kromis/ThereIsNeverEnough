import resources

class Draw_Comp:
    def __init__(self, comp_file_name, screen, position):
        self.screen = screen
        self.comp = resources.all_sprites[comp_file_name]
        self.position = position

        self.red = resources.all_sprites["componentRed.png"]
        self.green = resources.all_sprites["componentGreen.png"]
        self.glow = resources.all_sprites["componentGlow.png"]
        self.disable = resources.all_sprites["componentDisable.png"]
        self.disable.set_alpha(200)
        self.border = resources.all_sprites["component.png"]
        
    def draw(self, glowing, disabled):
        if glowing:
            self.screen.blit(self.glow, self.position)
            
        self.screen.blit(self.red, (self.position[0] + 25, self.position[1] + 25))
        self.screen.blit(self.green, (self.position[0] + 25, self.position[1] + 25), (0, 0, 100, 100))

        if disabled:          
            self.screen.blit(self.disable, (self.position[0] + 25, self.position[1] + 25))
        
        self.screen.blit(self.comp, (self.position[0] + 25, self.position[1] + 25))


        self.screen.blit(self.border, (self.position[0] + 25, self.position[1] + 25))

    def get_corners(self):
        return (self.position, (self.position[0] + 100, self.position[1] + 100))
