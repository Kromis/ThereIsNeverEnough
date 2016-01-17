import pygame
from Time import Time
from MonsterList import MonsterList
from CompartmentPackage import *
import Console

class Game:

    def __init__(self, screen):
        self.screen = screen
        self.activeRegions = {}
        self.allPackages = {}
        self.packageSelections = [ None, None, None ]
        self.initializePackages()
        self.console = Console.Console(self.screen) 

        self.time = Time()
        #tells Time to call "toggleDay" when 6:00 happens
        self.time.setToggleDayListener(self, '6:00')
        self.day = True

        self.monsterList = MonsterList()

    def addPackage(self, name, compType, position):
        package = CompartmentPackage(self.screen, compType, position)
        self.allPackages[name] = package
        self.activeRegions[package.get_corners()] = name


    def initializePackages(self):
        self.addPackage("Weapon", "weapon", (251, 521))
        #self.addPackage("Weapon", "weapon", (351, 521))
        #self.addPackage("Weapon", "weapon", (451, 521))

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

        for p in self.allPackages:            
            self.allPackages[p].update(p in self.packageSelections)

        self.monsterList.update(self.allPackages)
            
        for p in self.allPackages:
            self.allPackages[p].draw()
        self.console.draw()

        self.monsterList.draw()

    def toggleDay(self):
        self.day = not self.day
        print("DAY" if self.day else "NIGHT")




