

class Time:

    def __init__(self, hour = 12, minute = 0):
        self.hour = hour
        self.minute = minute

    def increment_minute(self):
        self.minute += 1

        if self.minute == 60:
            self.minute = 0
            self.increment_hour();

    def increment_hour(self):
        self.hour += 1

        if self.hour == 13:
            self.hour = 1

    def __str__(self):
        return '{:02d}:{:02d}'.format(self.hour, self.minute)


##T = Time()
##while(True):
##    input()
##    T.increment_minute()
##    print(T)
