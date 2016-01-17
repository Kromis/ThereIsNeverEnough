import pygame

class Time:

##    MS_PER_MINUTE = 300
    MS_PER_MINUTE = 0

    def __init__(self, hour = 12, minute = 0):
        self.hour = hour
        self.minute = minute

        self.next_update = pygame.time.get_ticks() + Time.MS_PER_MINUTE

        self.eventListener = None
        self.eventHour = None
        self.eventMinute = None

    def update(self):
        if (pygame.time.get_ticks() > self.next_update):
            self.increment_minute()
            self.next_update = pygame.time.get_ticks() + Time.MS_PER_MINUTE

        

    def setToggleDayListener(self, listener, time_as_str):
        self.eventListener = listener
        temp = time_as_str.split(':')
        self.eventHour = int(temp[0])
        self.eventMinute = int(temp[1])

    def increment_minute(self):
        self.minute += 1

        if self.minute == 60:
            self.minute = 0
            self.increment_hour();

    def increment_hour(self):
        self.hour += 1

        if self.hour == 13:
            self.hour = 1

        if self.eventListener != None and self.eventHour == self.hour:
            self.eventListener.toggleDay()


    def __str__(self):
        return '{:02d}:{:02d}'.format(self.hour, self.minute)

##T = Time()
##while(True):
##    input()
##    T.increment_minute()
##    print(T)
