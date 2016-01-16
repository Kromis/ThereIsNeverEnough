
class Room:
    MAX_HP = 100
    MIN_HP = 0
    def __init__(self, decrease=5, increase=10):
        self.alive = True
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


global allRooms
allRooms = {"Food" : Room(), "Weapon" : Room()}
global selectedRoom
selectedRoom = None

def incrementClock():
    for r in allRooms:
        room = allRooms[r]
        room.drain()
        if selectedRoom != None:
            allRooms[selectedRoom].fill()
    showRoomsStatus()

def showRoomsStatus():
    for r in allRooms:
        room = allRooms[r]
        print("{} Room\n  ->selected: {}\n  ->HP: {}".format(r, room.selected, str(room.hp)))
        if room.alive == False:
            print("  ->This room died :(")

def deselectRoom(name):
    allRooms[name].deselect()

def selectRoom(name):
    global selectedRoom
    if selectedRoom != None:
        deselectRoom(selectedRoom)
    selectedRoom = name
    allRooms[selectedRoom].select()

while True:
    response = input("\nEnter a response:\n-> ")
    if response == "q":
        break
    elif response == "":
        incrementClock()
    else:
        if response in allRooms.keys():
            print(response+" Room is selected.")
            selectRoom(response)
        else:
            print("Incorrect command.")
        
