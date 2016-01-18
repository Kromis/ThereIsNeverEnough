import random
import resources

class Compartment:
    def __init__(self, compType, decrease=0.2, increase=1, repairedHp=25, maxHp=100, minHp=0):
        self.compType = compType;
        self.MAX_CANNON_COOLDOWN = 1
        self.FIRING_HP_DECREASE = 5
        self.cannonCooldown = 0
        self.active = True
        self.MAX_HP = maxHp
        self.MIN_HP = minHp
        self.REPAIRED_HP = repairedHp
        self.RESTORE_SHIP_HP = 10
        self.hp = self.MAX_HP
        self.selected = False
        self.DECREASE = decrease
        self.INCREASE = increase
        self.runoutofpower = False

    def select(self):
        self.selected = True
        resources.sound_manager.playSound('select.ogg')
        self.runoutofpower = False
        
    def deselect(self):
        self.selected = False
        if not self.runoutofpower:
            resources.sound_manager.playSound('deselect.ogg')
        self.runoutofpower = True

    def toggleSelect(self):
        if self.selected:
            self.deselect()
        else:
            self.select()
    
        if self.compType == "light":
            self.use_light()


    def drain(self, dmg=0):
        self.hp -= dmg
        #self.hp -= self.DECREASE
        self.hp = max(self.hp, self.MIN_HP)
        if dmg > 0:
            self.checkActive()

    def fill(self):
        self.hp += self.INCREASE
        self.hp = min(self.hp, self.MAX_HP)
        if self.hp >= self.REPAIRED_HP:
            self.active = True

    def power(self):
        if self.selected:
            self.fill()
            if self.active:
                self.use()

    def update(self):
        if resources.game_manager.ship_power <= 0:
            self.deselect()
    
        if self.selected:
            if resources.game_manager.ship_power >= 1:
                resources.game_manager.ship_power -= 1
        self.drain()
        self.power()
        self.cannonCooldown += 1
        self.checkActive()

    def checkActive(self):
        if self.hp == self.MIN_HP:
            self.active = False
    
        if self.selected and self.compType == 'weapon':
            resources.game_manager.ship_reload += 1

    def use(self):
        pass

    def typeWeaponUse(self):
        if len(resources.game_manager.monsterList.list) > 0:
            
            if resources.game_manager.ship_reload >= 100:
                dmg = random.randint(20, 30)
                resources.sound_manager.playSound('cannon.ogg')
                resources.game_manager.ship_reload = 0

                
                if random.randint(1, 10) > resources.game_manager.cannon_accuracy:
                    resources.game_manager.cannonAttack(dmg)
                
    def use_light(self):
        if self.selected:
            resources.game_manager.night_opacity = 100
            resources.game_manager.cannon_accuracy = 1

        else:
            resources.game_manager.night_opacity = 200
            resources.game_manager.cannon_accuracy = 3

    def typeEngineUse(self):
        if self.active:
            resources.game_manager.ship_progress += 1

##        if self.cannonCooldown > self.MAX_CANNON_COOLDOWN and self.hp > self.FIRING_HP_DECREASE:
##            self.cannonCooldown = 0
##            dmg = random.randint(20, 30)
##            attacked = resources.game_manager.cannonAttack(dmg)
##            if attacked:
##                self.hp -= self.FIRING_HP_DECREASE
            

    def typeHealthUse(self):
        resources.game_manager.affectShipHp(self.RESTORE_SHIP_HP)
