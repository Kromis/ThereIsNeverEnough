import random
import resources

class Compartment:
    def __init__(self, decrease=0.2, increase=1, repairedHp=25, maxHp=100, minHp=0):
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

    def select(self):
        self.selected = True
    def deselect(self):
        self.selected = False

    def toggleSelect(self):
        self.selected = not self.selected

    def drain(self, dmg=0):
        self.hp -= dmg
        self.hp -= self.DECREASE
        self.hp = max(self.hp, self.MIN_HP)
        if dmg > 0:
            self.checkActive()
            resources.game_manager.affectShipHp(-dmg)

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
        if self.selected:
            resources.game_manager.ship_power -= 5
        self.drain()
        self.power()
        self.cannonCooldown += 1
        self.checkActive()

    def checkActive(self):
        if self.hp == self.MIN_HP:
            self.active = False
    
        if self.selected:
            resources.game_manager.ship_reload += 1

    def use(self):
        pass

    def typeWeaponUse(self):
        if len(resources.game_manager.monsterList.list) > 0:
            
            if resources.game_manager.ship_reload >= 100:
                dmg = random.randint(20, 30)

                if random.randint(1, 10) > 1:
                    resources.game_manager.cannonAttack(dmg)
                    resources.game_manager.ship_reload = 0
                


        
##        if self.cannonCooldown > self.MAX_CANNON_COOLDOWN and self.hp > self.FIRING_HP_DECREASE:
##            self.cannonCooldown = 0
##            dmg = random.randint(20, 30)
##            attacked = resources.game_manager.cannonAttack(dmg)
##            if attacked:
##                self.hp -= self.FIRING_HP_DECREASE
            

    def typeHealthUse(self):
        resources.game_manager.affectShipHp(self.RESTORE_SHIP_HP)
