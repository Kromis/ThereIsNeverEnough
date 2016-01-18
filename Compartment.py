import random
import resources

class Compartment:
    def __init__(self, compType, decrease=0.2, increase=1, repairedHp=25, maxHp=100, minHp=0):
        self.compType = compType;
        self.FIRING_HP_DECREASE = 5
        self.active = True
        self.MAX_HP = maxHp
        self.MIN_HP = minHp
        self.MIN_DMG = 30
        self.MAX_DMG = 40
        self.REPAIRED_HP = repairedHp
        self.RESTORE_SHIP_HP = 0.2
        self.hp = self.MAX_HP
        if compType == "engine":
            self.selected = True
        else:
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
        if self.compType == "light":
            self.use_light()

    def toggleSelect(self):
        if self.selected:
            self.deselect()
        else:
            self.select()
    
        if self.compType == "light":
            self.use_light()


    def drain(self, dmg=0):
        self.hp -= dmg
        self.hp -= self.DECREASE
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
            if resources.game_manager.ship_power >= 0:
                if self.compType == "light":
                    resources.game_manager.ship_power -= .5
                else:
                    resources.game_manager.ship_power -= 1
        self.drain()
        self.power()
        self.checkActive()

    def checkActive(self):
        if self.hp == self.MIN_HP:
            self.active = False
    
        if self.selected and self.compType == 'weapon':
            resources.game_manager.ship_reload += 2
            
            if resources.game_manager.ship_reload >= 100:
                resources.game_manager.ship_reload = 100

    def use(self):
        pass

    def typeWeaponUse(self):
        if len(resources.game_manager.monsterList.list) > 0:
            
            if resources.game_manager.ship_reload >= 100:
                dmg = random.randint(self.MIN_DMG, self.MAX_DMG)
                resources.sound_manager.playSound('cannon.ogg')
                resources.game_manager.ship_reload = 0

                
                #if random.randint(1, 10) > resources.game_manager.cannon_accuracy:
                resources.game_manager.cannonAttack(dmg)

        
    def use_light(self):
        if self.selected:
            resources.game_manager.night_opacity = 100
            #resources.game_manager.cannon_accuracy = 1

        else:
            resources.game_manager.night_opacity = resources.game_manager.OPACITY    
            #resources.game_manager.cannon_accuracy = 3

    def typeEngineUse(self):
        if self.active:
            resources.game_manager.ship_progress += 1
            if resources.game_manager.ship_progress >= resources.game_manager.SHIP_MAX_PROGRESS:
                resources.game_manager.ship_progress =  resources.game_manager.SHIP_MAX_PROGRESS

    def typeHealthUse(self):
        resources.game_manager.affectShipHp(self.RESTORE_SHIP_HP)
