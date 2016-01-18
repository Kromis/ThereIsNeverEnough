import random
import pygame
from Enemy import Enemy
import resources

class MonsterList:

    AVG_ENCOUNTER_TIME = 10000 #15 seconds
    ENCOUNTER_TIME_VARIANCE = 10000  #+/- 5 seconds

    MAX_MONSTERS = 2

    def __init__(self):
        self.list = []

        self.updateTimeBetweenEncounters()
        self.previousTime = pygame.time.get_ticks()

    def addMonster(self, monster):
        if len(self.list) < MonsterList.MAX_MONSTERS:
            self.list.insert(0, monster)
            #print("NEW MONSTER ENCOUNTER")
            #update monster positions
            for v in range(len(self.list)):
                self.list[v].newPos = (resources.width-350, resources.height-200-(100*v))
            return True

    def update(self):
        self.randomEncounter()
        for monster in self.list:
            dmg = monster.update()
            if dmg > 0:
                resources.game_manager.enemyAttack(dmg)

    def draw(self):
        for m in self.list:
            m.draw()


    def updateTimeBetweenEncounters(self):
        self.timeBetweenEncounters = MonsterList.AVG_ENCOUNTER_TIME + \
                                    random.randint(-MonsterList.ENCOUNTER_TIME_VARIANCE, \
                                                   MonsterList.ENCOUNTER_TIME_VARIANCE)

    def randomEncounter(self):
        now = pygame.time.get_ticks()
        if now - self.previousTime >= self.timeBetweenEncounters:
            self.previousTime = now
            enemySpawned = self.addMonster(Enemy())
            if enemySpawned:
                resources.game_manager.messages.append([None, None, "Flavor", "Enemy has appeared!"])
            self.updateTimeBetweenEncounters()
        
    def attackOldestMonster(self, dmg):
        if len(self.list) > 0:
            #print("Attack!")
            active = self.list[-1].take_damage(dmg)

    def removeMonster(self):
        self.list.pop()