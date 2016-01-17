import pygame
from Time import Time
from MonsterList import MonsterList
from CompartmentPackage import *
from Enemy import *
import Console
import resources


class Game:
    def reset(self):
        self.screen = resources.screen
        self.activeRegions = {}
        self.allPackages = {}
        self.allPackageNames = []
        self.packageSelections = [ None, None, None ]
        self.attackablePackageNames = {}
        self.allShields = []
        self.messages = []

        self.shipHp = 500
        self.ship_power = 500
        
        self.initializePackages()
        self.console = Console.Console(self.screen) 


        self.time = resources.time
        #tells Time to call "toggleDay" when 6:00 happens
        self.time.setToggleDayListener(self, '6:00')
        self.day = True


        self.monsterList = MonsterList()

    def __init__(self):
        self.reset()

    def addPackage(self, name, compType, position):
        package = CompartmentPackage(self.screen, compType, position)
        self.allPackages[name] = package
        self.activeRegions[package.get_corners()] = name
        self.allPackageNames.append(name)
        if compType == "shield":
            self.allShields.append(name)

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
        # update stuff
        self.time.update()
        self.console.get_message(self.messages)

        for name in self.allPackages:            
            active = self.allPackages[name].update(name in self.packageSelections)
            if active:
                self.attackablePackageNames[name] = True
            elif name in self.attackablePackageNames:
                self.attackablePackageNames.pop(name, None)
        self.monsterList.update()

        # draw stuff
        for p in self.allPackages:
            self.allPackages[p].draw()
        self.monsterList.draw()
        self.console.draw()
        

    def toggleDay(self):
        self.day = not self.day
        print("DAY" if self.day else "NIGHT")


    def enemyAttack(self, dmg):
        if len(self.attackablePackageNames) == 0:
            self.attackShip(dmg)
            print("Your ship is attacked! Current health left: {}:".format(self.shipHp))
        else:
            for shieldName in self.allShields:
                if shieldName in self.attackablePackageNames:
                    self.allPackages[shieldName].attacked(dmg)
                    return
            name = random.choice(list(self.attackablePackageNames.keys()))
            self.allPackages[name].attacked(dmg)
            print("Compartment '{}' is attacked!".format(name))
    def attackShip(self, dmg):
        self.shipHp -= dmg
        if self.shipHp <= 0:
            print("You died")

    def cannonAttack(self, dmg):
        return self.monsterList.attackOldestMonster(dmg)


