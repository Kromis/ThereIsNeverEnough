import random

class Compartment:
    def __init__(self, game_manager, decrease=5, increase=10, repairedHp=100, maxHp=100, minHp=0):
        self.MAX_CANNON_COOLDOWN = 1
        self.FIRING_HP_DECREASE = 5
        self.cannonCooldown = 0
        self.game_manager = game_manager
        self.active = True
        self.MAX_HP = maxHp
        self.MIN_HP = minHp
        self.REPAIRED_HP = repairedHp
        self.hp = self.MAX_HP
        self.selected = False
        self.DECREASE = decrease
        self.INCREASE = increase

    def select(self):
        self.selected = True
    def deselect(self):
        self.selected = False
    

    def drain(self, dmg=0):
        self.hp -= dmg
        if dmg > 0:
            self.hp -= self.DECREASE
        self.hp = max(self.hp, self.MIN_HP)

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
        self.drain()
        self.power()
        self.cannonCooldown += 1
        if self.hp == self.MIN_HP:
            self.active = False

    def use(self):
        pass

    def typeWeaponUse(self):
        if self.cannonCooldown > self.MAX_CANNON_COOLDOWN and self.hp > self.FIRING_HP_DECREASE:
            self.hp -= self.FIRING_HP_DECREASE
            self.cannonCooldown = 0
            dmg = random.randint(20, 30)
            self.game_manager.cannonAttack(dmg)
