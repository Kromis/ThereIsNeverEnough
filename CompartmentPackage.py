from Compartment import *

class CompartmentPackage:
    def __init__(self):
        self.GUI = None #DrawObject
        self.compartment = Compartment()

    def update(self, selected):
        self.compartment.update()
        #self.GUI.update()

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
