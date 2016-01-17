import pygame
from Time import Time
from MonsterList import MonsterList
from CompartmentPackage import *
from Enemy import *
import Console
import resources
from Time import Time

class Game:
    def reset(self):
        self.screen = resources.screen
        self.activeRegions = {}
        self.allPackages = {}
        self.allPackageNames = []
        self.allShields = []
        self.messages = []

        self.MAX_SHIP_HP = 100
        self.shipHp = 100
        self.MAX_SHIP_POWER = 1400
        self.ship_power = 1400
        self.ship_reload = 0
        self.SHIP_MAX_PROGRESS = 500
        self.ship_progress = 0
        self.night_opacity = 200

        self.cannon_accuracy = 3
        
        self.console = Console.Console(self.screen) 
        
        resources.time = Time()
        self.time = resources.time
        #tells Time to call "toggleDay" when 6:00 happens
        self.time.setToggleDayListener(self, '6:00')
        self.day = False
        self.night = resources.all_sprites["night.png"]

        self.monsterList = MonsterList()

        self.initializePackages()

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

        self.addPackage("Weapon 2", "weapon", (708, 470))
        self.addPackage("Weapon", "weapon", (588, 470))
        self.addPackage("Health 2", "health", (468, 500))
        self.addPackage("Health", "health", (348, 500))
        self.addPackage("Shield", "shield", (228, 500))
        self.addPackage("Engine", "engine", (108, 500))
        self.addPackage("Light", "light", (443, 375))

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
            print(name+" selected :)")
            self.allPackages[name].compartment.toggleSelect()
            break
            
    def update(self):
        # update stuff
        self.time.update()
        self.console.get_message(self.messages)
        
        if self.day:
            if (self.ship_power < self.MAX_SHIP_POWER):
                self.ship_power += 2

        for name in self.allPackages:            
            self.allPackages[name].update(name)

        self.night.set_alpha(self.night_opacity)

        self.monsterList.update()
        
        if self.ship_progress >= self.SHIP_MAX_PROGRESS:
            resources.state = "WIN"
        elif self.shipHp <= 0:
            resources.state = "LOSE"

        # draw stuff
        for p in self.allPackages:
            if p != "Light":
                self.allPackages[p].draw()
        self.allPackages["Light"].draw()
        self.monsterList.draw()
        self.console.draw()
        

    def toggleDay(self):
        self.day = not self.day
        if self.day:
            self.cannon_accuracy = 1
        else:
            self.cannon_accuracy = 3
        print("DAY" if self.day else "NIGHT")


    def enemyAttack(self, dmg):

        for shieldName in self.allShields:
            if self.allPackages[shieldName].compartment.active:
                self.allPackages[shieldName].attacked(dmg)
                return
        self.text = "Your ship is damaged! Current health left: {}".format(self.shipHp)
        self.messages.append(["None", "None", "Damaged", self.text])
        print("Your ship is attacked! Current health left: {}".format(self.shipHp))
        self.affectShipHp(-dmg)

         
        for name in self.allPackages:
            dmg += random.randint(-5, 5)
            self.allPackages[name].attacked(dmg)
            
    def affectShipHp(self, value):
        self.shipHp += value
        self.shipHp = max(self.shipHp, 0)
        self.shipHp = min(self.MAX_SHIP_HP, self.shipHp)
        if self.shipHp <= 0:
            print("You died")

    def cannonAttack(self, dmg):
        return self.monsterList.attackOldestMonster(dmg)


