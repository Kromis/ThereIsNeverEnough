import resources

class Draw_Comp:
    def __init__(self, comp_type, screen, position):
        self.screen = screen
        self.comp = resources.all_sprites[comp_type]
        self.position = position

        self.red = resources.all_sprites["componentRed.png"]
        self.green = resources.all_sprites["componentGreen.png"]
        self.glow = resources.all_sprites["componentGlow.png"]
        self.disable = resources.all_sprites["componentDisable.png"]
        self.border = resources.all_sprites["component.png"]
        
    def draw(self):
        self.screen.blit(self.glow, self.position)
        self.screen.blit(self.disable, self.position)
        self.screen.blit(self.red, self.position)
        self.screen.blit(self.green, self.position, (0, 0, 50, 50))
