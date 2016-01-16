from CompartmentPackages import *

class Game:
    def __init__(self):
        self.activeRegions = {}
        self.allPackages = {}
        self.packageSelections = [ None, None, None ]

    def addPackage(self, name, compType, xy):
        package = CompartmentPackage(compType, xy)
        self.allPackages[name] = package
    
    def initializePackages(self):
        addPackage("Weapon", "weapon", (x, y))
                
