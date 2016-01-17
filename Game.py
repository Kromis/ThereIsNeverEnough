from CompartmentPackages import *

class Game:
    def __init__(self):
        self.activeRegions = {}
        self.allPackages = {}
        self.packageSelections = [ None, None, None ]
        self.day = True

    def addPackage(self, name, compType, position):
        package = CompartmentPackage(compType, position)
        self.allPackages[name] = package
        self.activeRegions[package.get_corners()] = name
    
    def initializePackages(self):
        position = (0, 0)
        addPackage("Weapon", "weapon", position)

    def click(self, position):
        for name in self.activeRegions:
            region = self.activeRegions[name]
            x = position[0]
            y = position[1]
            if x < region[0][0]:
                continue
            if x > region[1][0]:
                continue
            if y < region[0][1]:
                continue
            if y > region[1][1]:
                continue
            if name not in self.packageSelections:
                self.packageSelections.insert(0, name)
                removed = self.packageSelections.pop()
                allPackages[removed].deselect()
                allPackages[name].select()
            break
            
    def update(self):
        for p in allPackages:
            allPackages[p].update()
        for p in allPackages:
            allPackages[p].draw()
