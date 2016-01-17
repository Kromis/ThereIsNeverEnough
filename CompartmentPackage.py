from Compartment import *
from Draw_Comp import *

class CompartmentPackage:

    def __init__(self, screen, compType, position):
        self.type = compType
        self.GUI = None #DrawObject

        self.compartment = Compartment()
        self.screen = screen


        file_name = None
        if compType == "weapon":
            self.compartment.use = self.compartment.typeWeaponUse
            file_name = "cannon.png"
            
        elif compType == "shield":
            file_name = "shield.png"

        elif compType == "health":
            self.compartment.use = self.compartment.typeHealthUse
            file_name = "health.png"

        elif compType == "engine":
            file_name = "engine.png"

        elif compType == "light":
            file_name = "light.png"

        self.GUI = Draw_Comp(file_name, self.screen, position)

    def update(self, selected):
        self.compartment.update()
        return self.active()

    def draw(self):

        self.GUI.draw(self.compartment.selected, not self.compartment.active, self.compartment, self.compartment.MAX_HP)

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
