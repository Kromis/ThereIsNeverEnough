
class Enemy:

    DEFAULT_HEALTH = 100
    DEFAULT_DAMAGE = 20
    
    def __init__(self):
        self.x = 0
        self.y = 0
        self.hp = Enemy.DEFAULT_HEALTH
        self.damage = Enemy.DEFAULT_DAMAGE
        self.delay = 5
        self.type = ''

    def update(self):
        if (self.hp <= 0):
            print('Dead')
        print('Updating')
        
    def attack(self, thing):
        thing.hp -= self.damage

    def take_damage(self, damage):
        self.hp -= damage
