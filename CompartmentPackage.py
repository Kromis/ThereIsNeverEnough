from Compartment import *
from Draw_Comp import *

class CompartmentPackage:
    def __init__(self, screen, compType, position):
        self.type = compType
        self.GUI = None #DrawObject
        self.compartment = Compartment()
        self.screen = screen
        
        if compType == "weapon":
            # bind comp.use() to attacking enemy
            self.GUI = Draw_Comp("cannon.png", self.screen, position)

    def update(self, selected):
        self.compartment.update()

    def draw(self):
        self.GUI.draw(self.compartment.selected, not self.compartment.active)
    
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
