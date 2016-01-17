from CompartmentPackage import *

class Game:
    def __init__(self):
        self.activeRegions = {}
        self.allPackages = {}
        self.packageSelections = [ None, None, None ]
        self.day = True

    def addPackage(self, name, compType, position):
        package = CompartmentPackage(compType, position)
        self.allPackages[name] = package
    
    def initializePackages(self):
        position = (0, 0)
        addPackage("Weapon", "weapon", position)
                
    def update(self):
        for p in self.allPackages:
            p.draw()
