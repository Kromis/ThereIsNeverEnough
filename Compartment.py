class Compartment:
    def __init__(self, decrease=5, increase=10, repairedHp=50, maxHp=100, minHp=0):
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
    
    def drain(self):
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
        if self.hp == self.MIN_HP:
            self.active = False

    def use(self):
        print("This compartment is doing hard work")
        pass
