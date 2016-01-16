from CompartmentPackages import *

class Game:
    def __init__(self):
        self.activeRegions = {}
        self.allPackages = []
        self.packageSelections = [ None, None, None ]

    def addPackage(self):
        package = CompartmentPackage()
        # insert other details such as block x,y
        self.allPackages.Add(package)
        pass
    
    def initializePackages(self):
        weaponCompartment = ("Weapon")
                
