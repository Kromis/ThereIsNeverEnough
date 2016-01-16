from CompartmentPackage import *

def updateAll():
    global allPackages
    for p in allPackages:
        package = allPackages[p]
        selected = False
        if p == selectedPackage:
            selected = True
        package.update(selected)
    showRoomsStatus()

def showRoomsStatus():
    for p in allPackages:
        package = allPackages[p]
        print("{} Compartment\n  ->selected: {}\n  ->HP: {}".format(p, package.selected(), str(package.compartment.hp)))
        if package.active == False:
            print("  ->This compartment is down :(")

def deselect(name):
    allPackages[name].deselect()

def select(name):
    global selectedPackage
    if selectedPackage != None:
        deselect(selectedPackage)
    selectedPackage = name
    allPackages[name].select()

if __name__ == "__main__":
    global allPackages
    allPackages = {"Food" : CompartmentPackage(), "Weapon" : CompartmentPackage()}
    global selectedPackage
    selectedPackage = None
    
    while True:
        response = input("\nEnter a response:\n-> ")
        if response == "q":
            break
        elif response == "":
            updateAll()
        else:
            if response in allPackages.keys():
                print(response+" Package is selected.")
                select(response)
            else:
                print("Incorrect command.")
        
