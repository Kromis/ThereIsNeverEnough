
class Enemy:

    DEFAULT_HEALTH = 100
    DEFAULT_DAMAGE = 20
    
    def __init__(self, delay=5):
        self.x = 0
        self.y = 0
        self.hp = Enemy.DEFAULT_HEALTH
        self.damage = Enemy.DEFAULT_DAMAGE
        self.delay = delay
        self.delayCounter = 0
        self.type = ''
        self.alive = True

    def update(self):
        if (self.hp <= 0):
            self.alive = False
            #print('Dead')
            #print('Updating')
        self.delayCounter += 1
        if self.delayCounter > self.delay:
            self.delayCounter = 0
            return True
        return False

    def draw(self):
        pass
        
    def attack(self, thing):
        thing.hp -= self.damage

    def take_damage(self, damage):
        self.hp -= damage

    def is_dead(self):
        return not self.alive
