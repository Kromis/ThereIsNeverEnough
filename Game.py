import pygame
import random
from Time import Time
from CompartmentPackage import *
from Enemy import *
import Console

class Game:

    AVG_ENCOUNTER_TIME = 10000 #10 seconds
    ENCOUNTER_TIME_VARIANCE = 5000  #+/- 5 seconds
    
    def __init__(self, screen):
        self.screen = screen
        self.activeRegions = {}
        self.allPackages = {}
        self.allPackageNames = []
        self.packageSelections = [ None, None, None ]
        self.allEnemies = [ None, None, None ]
        self.attackablePackageNames = {}

        self.shipHp = 100
        
        self.initializePackages()
        self.console = Console.Console(self.screen) 

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
        self.allPackageNames.append(name)
    def initializePackages(self):
        self.addPackage("Weapon", "weapon", (251, 521))
        self.addPackage("Weapon2", "weapon", (351, 521))
        self.addPackage("Weapon3", "weapon", (451, 521))
        self.addPackage("Weapon4", "weapon", (551, 521))

    def spawnEnemy(self):
        if None in self.allEnemies:
            self.allEnemies.insert(0, Enemy())
            self.allEnemies.pop()

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
        self.randomEncounter()
        for name in self.allPackages:            
            active = self.allPackages[name].update(name in self.packageSelections)
            if active:
                self.attackablePackageNames[name] = True
            elif name in self.attackablePackageNames:
                self.attackablePackageNames.pop(name, None)
        for enemy in self.allEnemies:
            if enemy == None:
                break
            attack = enemy.update()
            if attack:
                self.enemyAttack()

        # draw stuff
        for p in self.allPackages:
            self.allPackages[p].draw()
        for enemy in self.allEnemies:
            pass
            #draw enemy
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
            self.spawnEnemy()

    def enemyAttack(self):
        dmg = random.randint(10, 15)
        if len(self.attackablePackageNames) == 0:
            self.attackShip(dmg)
            print("Your ship is attacked! Current health left: {}:".format(self.shipHp))
        else:
            name = random.choice(list(self.attackablePackageNames.keys()))
            self.allPackages[name].attacked(dmg)
            print("Compartment '{}' is attacked!".format(name))
        
    def attackShip(self, dmg):
        self.shipHp -= dmg
        if self.shipHp <= 0:
            print("You died")

