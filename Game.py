from Time import Time
from CompartmentPackage import *


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.activeRegions = {}
        self.allPackages = {}
        self.packageSelections = [ None, None, None ]
        self.initializePackages()

        self.time = Time()
        #tells Time to call "toggleDay" when 6:00 happens
        self.time.setToggleDayListener(self, '6:00')
        
        self.day = True

    def addPackage(self, name, compType, position):
        package = CompartmentPackage(self.screen, compType, position)
        self.allPackages[name] = package
        self.activeRegions[((0,0),(100,100))] = name#package.get_corners()] = name
    
    def initializePackages(self):
        position = (0, 0)
        self.addPackage("Weapon", "weapon", position)

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
        self.time.update()
        for p in self.allPackages:            
            self.allPackages[p].update(p in self.packageSelections)
        for p in self.allPackages:
            self.allPackages[p].draw()

    def toggleDay(self):
        self.day = not self.day
        print("DAY" if self.day else "NIGHT")

