from Compartment import *
from Draw_Comp import *

class CompartmentPackage:
    def __init__(self, game_manager, screen, compType, position):
        self.game_manager = game_manager
        self.type = compType
        self.GUI = None #DrawObject
        self.compartment = Compartment(self.game_manager)
        self.screen = screen
        
        if compType == "weapon":
            self.compartment.use = self.compartment.typeWeaponUse
            self.GUI = Draw_Comp("cannon.png", self.screen, position)

    def update(self, selected):
        self.compartment.update()
        return self.active()

    def draw(self):
        self.GUI.draw(self.compartment.selected, not self.compartment.active)

    def attacked(self, dmg):
        self.compartment.drain(dmg)
    
    # Getters
    def selected(self):
        return self.compartment.selected
    def active(self):
        return self.compartment.active
    def get_corners(self):
        return self.GUI.get_corners()

    # Setters
    def select(self):
        self.compartment.select()
    def deselect(self):
        self.compartment.deselect()
