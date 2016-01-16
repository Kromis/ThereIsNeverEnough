class Room:
    def __init__(self, decrease=5, increase=10, MAX_HP=100, MIN_HP=0):
        self.alive = True
        self.MAX_HP = MAX_HP
        self.MIN_HP = MIN_HP
        self.hp = self.MAX_HP
        self.selected = False
        self.DECREASE = decrease
        self.INCREASE = increase
        
    def drain(self):
        self.hp -= self.DECREASE
        if self.hp <= self.MIN_HP:
            self.alive = False
            self.hp = self.MIN_HP
            return False

    def fill(self):
        if self.alive == False:
            print("This room already died, you can't revive it.")
            return
        if self.selected:
            self.hp += self.INCREASE
        if self.hp > self.MAX_HP:
            self.hp = self.MAX_HP

    def select(self):
        self.selected = True
    def deselect(self):
        self.selected = False
