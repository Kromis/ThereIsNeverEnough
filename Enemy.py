import random
import resources

class Enemy:
    DEFAULT_HEALTH = 100
    DEFAULT_DAMAGE = 20
    
    def __init__(self, delay=20):
        self.x = 0
        self.y = 0
        self.hp = Enemy.DEFAULT_HEALTH
        self.damage = Enemy.DEFAULT_DAMAGE
        self.delay = delay
        self.delayCounter = 0
        self.type = ''
        self.alive = True
        self.MIN_DMG = 5
        self.MAX_DMG = 8

        self.screen = resources.screen
        self.sprite = resources.all_sprites["tentacle.png"]
        self.position = (resources.width-350, resources.height-200)
        self.newPos = self.position
        self.SHIFT = (2,5)
        
    def update(self):
        #gradually shift tentacles
        x = self.position[0]
        y = self.position[1]
        if self.newPos[0] > self.position[0]:
            x += self.SHIFT[0]
        if self.newPos[1] < self.position[1]:
            y -= self.SHIFT[1]
        self.position = (x, y)
        
        if (self.hp <= 0):
            self.alive = False
            #print('Dead')
            #print('Updating')
        self.delayCounter += 1
        if self.delayCounter > self.delay:
            self.delayCounter = 0
            return self.attack()
        return False

    def draw(self):
        if not resources.game_manager.day:
            if resources.game_manager.allPackages["Light"].compartment.selected:
                resources.screen_copied.blit(resources.all_sprites["glow.png"], (self.position[0], self.position[1] - 100))
        resources.screen_copied.blit(self.sprite, self.position)
        
    def attack(self):
        damage = random.randint(self.MIN_DMG, self.MAX_DMG)
        return damage

    def take_damage(self, damage):
        self.hp -= damage
        self.newPos = (resources.width-(350*self.hpPercentage()), self.newPos[1])
        self.hp = max(self.hp, 0)
        if self.hp == 0:
            self.alive = False
        return self.alive

    def is_dead(self):
        return not self.alive

    def hpPercentage(self):
        return self.hp/Enemy.DEFAULT_HEALTH
