from Time import Time
from CompartmentPackage import *


class Game:
    def __init__(self):
        self.activeRegions = {}
        self.allPackages = {}
        self.packageSelections = [ None, None, None ]

        self.time = Time()
        #tells Time to call "toggleDay" when 6:00 happens
        self.time.setToggleDayListener(self, '6:00')
        
        self.day = True

    def addPackage(self, name, compType, position):
        package = CompartmentPackage(compType, position)
        self.allPackages[name] = package
    
    def initializePackages(self):
        position = (0, 0)
        addPackage("Weapon", "weapon", position)
                
    def update(self):
        #print(self.time)
        self.time.update()
        for p in self.allPackages:
            p.draw()

    def toggleDay(self):
        self.day = not self.day
        print("DAY" if self.day else "NIGHT")
