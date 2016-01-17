import pygame
import random
from Time import Time
from CompartmentPackage import *
import Console

class Game:

    AVG_ENCOUNTER_TIME = 10000 #10 seconds
    ENCOUNTER_TIME_VARIANCE = 5000  #+/- 5 seconds
    
    def __init__(self, screen):
        self.screen = screen
        self.activeRegions = {}
        self.allPackages = {}
        self.packageSelections = [ None, None, None ]
        self.initializePackages()
        self.console = Console.Console(self.screen) 

        self.ship_health = 30
        self.ship_power = 100

        self.time = Time()
        #tells Time to call "toggleDay" when 6:00 happens
        self.time.setToggleDayListener(self, '6:00')
        self.day = True

        self.updateTimeBetweenEncounters()
        self.previousTime = pygame.time.get_ticks()

    def addPackage(self, name, compType, position):
        package = CompartmentPackage(self.screen, compType, position)
        self.allPackages[name] = package
        self.activeRegions[package.get_corners()] = name
    
    def initializePackages(self):
        self.addPackage("Weapon", "weapon", (580, 470))
        self.addPackage("Weapon 2", "weapon", (700, 470))
        self.addPackage("Shield", "shield", (200, 500))

    def click(self, position):
        for region in self.activeRegions:
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
            name = self.activeRegions[region]
            if name not in self.packageSelections:
                print(name+" selected :)")
                self.packageSelections.insert(0, name)
                removed = self.packageSelections.pop()
                if removed != None:
                    self.allPackages[removed].deselect()
                self.allPackages[name].select()
            break
            
    def update(self):
        self.time.update()
        self.randomEncounter()
        for p in self.allPackages:            
            self.allPackages[p].update(p in self.packageSelections)
        for p in self.allPackages:
            self.allPackages[p].draw()
        self.console.draw()

    def toggleDay(self):
        self.day = not self.day
        print("DAY" if self.day else "NIGHT")

    def updateTimeBetweenEncounters(self):
        self.timeBetweenEncounters = Game.AVG_ENCOUNTER_TIME + \
                                    random.randint(-Game.ENCOUNTER_TIME_VARIANCE, \
                                                   Game.ENCOUNTER_TIME_VARIANCE)

        
    def randomEncounter(self):
        now = pygame.time.get_ticks()
        if now - self.previousTime >= self.timeBetweenEncounters:
            self.previousTime = now
            print("ENCOUNTER")
            self.updateTimeBetweenEncounters()
        


