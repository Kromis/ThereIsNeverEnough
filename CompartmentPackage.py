from Compartment import *

class CompartmentPackage:
    def __init__(self, screen, compType, position):
        self.type = compType
        self.compartment = Compartment()
        if compType == "weapon":
            # bind comp.use() to attacking enemy
            self.GUI = Draw_Comp(screen, "cannon.png", position)

    def update(self, selected):
        self.compartment.update()
        
    def draw(self):
        self.GUI.draw()

    # Getters
    def selected(self):
        return self.compartment.selected
    def active(self):
        return self.compartment.active

    # Setters
    def select(self):
        self.compartment.select()
    def deselect(self):
        self.compartment.deselect()
