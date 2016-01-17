import random
import pygame
from Enemy import Enemy

class MonsterList:

    AVG_ENCOUNTER_TIME = 10000 #10 seconds
    ENCOUNTER_TIME_VARIANCE = 5000  #+/- 5 seconds

    MAX_MONSTERS = 3

    def __init__(self):
        self.list = []

        self.updateTimeBetweenEncounters()
        self.previousTime = pygame.time.get_ticks()

    def addMonster(self, monster):
        if len(self.list) < MonsterList.MAX_MONSTERS:
            self.list.append(monster)
            print("NEW MONSTER ENCOUNTER")

    def update(self, compartments):
        self.randomEncounter()


        i = 0
        while(i < len(self.list)):
            if (self.list[i].is_dead()):
                self.list.pop(i)
            else:
                self.list[i].update(compartments)
                i += 1 

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
            self.addMonster(Enemy())
            self.updateTimeBetweenEncounters()
        
