import pygame
from Time import Time
from MonsterList import MonsterList
from CompartmentPackage import *
from Enemy import *
import Console
import resources
from Time import Time
from ScreenShaker import *
from Background import Background

class Game:
    def reset(self):
        self.shakeScreen = resources.screen
        self.screen = self.shakeScreen.copy()
        resources.screen_copied = self.screen
        self.background = Background(self.screen)
        self.screenShaker = ScreenShaker()
        
        self.OPACITY = 250
        
        self.activeRegions = {}
        self.allPackages = {}
        self.allPackageNames = []
        self.allShields = []
        self.messages = []

        self.MAX_SHIP_HP = 100
        self.shipHp = 100
        self.MAX_SHIP_POWER = 1000
        self.ship_power = 1000
        self.ship_reload = 0
        self.SHIP_MAX_PROGRESS = 2000
        self.ship_progress = 0
        self.night_opacity = self.OPACITY

        #self.cannon_accuracy = 3
        
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
        self.addPackage("Health", "health", (468, 500))
        self.addPackage("Shield 2", "shield", (228, 500))
        self.addPackage("Shield", "shield", (348, 500))
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
            #print(name+" selected :)")
            self.allPackages[name].compartment.toggleSelect()
            break
            
    def update(self):
        self.background.update()
        self.background.draw()
    
    
    
        # update stuff
        self.time.update()
        self.console.get_message(self.messages)
        
        if self.day:
            if (self.ship_power < self.MAX_SHIP_POWER):
                self.ship_power += 5.5
                if self.ship_power > self.MAX_SHIP_POWER:
                    self.ship_power = self.MAX_SHIP_POWER

        for name in self.allPackages:
            self.allPackages[name].update(name)

        self.night.set_alpha(self.night_opacity)

        self.monsterList.update()
        
        if self.ship_progress >= self.SHIP_MAX_PROGRESS:
            resources.state = "WIN"
            resources.sound_manager.playSound('win.ogg')

        elif self.shipHp <= 0:
            resources.state = "LOSE"
            resources.sound_manager.playSound('lose.ogg')

        # draw stuff
        for p in self.allPackages:
            if p != "Light":
                self.allPackages[p].draw()

        self.monsterList.draw()
        self.allPackages["Light"].draw()

        if self.ship_progress == self.SHIP_MAX_PROGRESS/2:
            self.messages.append([None, None, "Flavor", "You're halfway home... You can do this."])
        
        if self.ship_power >= self.MAX_SHIP_POWER/2 -1 and self.ship_power <= self.MAX_SHIP_POWER/2 + 1:
            self.messages.append([None, None, "Flavor", "Your power is getting low. Be careful."])
        
        self.console.draw()
        
        self.screenShaker.update()
        self.shakeScreen.blit(self.screen, self.screenShaker.getValue())

    def toggleDay(self):
        self.day = not self.day
        #if self.day:
         #   self.cannon_accuracy = 1
        #else:
        #    self.cannon_accuracy = 3
        #print("DAY" if self.day else "NIGHT")


    def enemyAttack(self, dmg):
        resources.sound_manager.playSound('tentacle.ogg')

        for shieldName in self.allShields:
            if self.allPackages[shieldName].compartment.active:
                self.screenShaker.shake()
                self.allPackages[shieldName].attacked(dmg* 3)
                self.affectShipHp(-dmg/3)
                for comp in self.allPackages:
                    if self.allPackages[comp].compartment.active == False and not self.allPackages[comp].compartment.currentlyDisabled:
                        self.allPackages[comp].compartment.currentlyDisabled = True
                        comp_type = self.allPackages[comp].compartment.compType
                        first_letter = comp_type[0].upper()
                        self.messages.append([None, None, "Flavor", first_letter + comp_type[1:] + " has been disabled."])
                return

        self.screenShaker.shake(6, 2000)
        if self.shipHp < self.MAX_SHIP_HP/4:
            self.text = "Your ship is in critical health.".format(int(self.shipHp))
            self.messages.append(["None", "None", "Damaged", self.text])



##        self.text = "Your ship is damaged! Current health left: {}".format(self.shipHp)
##        self.messages.append(["None", "None", "Damaged", self.text])
        #print("Your ship is attacked! Current health left: {}".format(self.shipHp))
        self.affectShipHp(-dmg * 2)

         
        for name in self.allPackages:
            dmg += random.randint(-5, 5)
            self.allPackages[name].attacked(dmg)

        for comp in self.allPackages:
            if self.allPackages[comp].compartment.active == False and not self.allPackages[comp].compartment.currentlyDisabled:
                self.allPackages[comp].compartment.currentlyDisabled = True
                comp_type = self.allPackages[comp].compartment.compType
                first_letter = comp_type[0].upper()
                self.messages.append([None, None, "Flavor", first_letter + comp_type[1:] + " has been disabled."])
                
    def affectShipHp(self, value):
        self.shipHp += value
        self.shipHp = max(self.shipHp, 0)
        self.shipHp = min(self.MAX_SHIP_HP, self.shipHp)
        if self.shipHp <= 0:
            pass
            #print("You died")

    def cannonAttack(self, dmg):
        self.monsterList.attackOldestMonster(dmg)


