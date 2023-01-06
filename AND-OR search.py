import random


def checkstate(currentstate):
    for i in l:
        if (i==currentstate):
            return 0

    l.append(currentstate)
    return 1

def printInformation(location):
    print("Location " + location + " is Dirty.")
    print("Cost for CLEANING " + location + ": 1")
    print("Location " + location + " has been Cleaned.")


def vacuumCleaner(goalState, currentState, location):
    # printing necessary data
    print("Goal State Required:", goalState)
    print("Vacuum is placed in Location " + location)

    # cleaning locations
    totalCost = 0
    while (currentState != goalState):
        if (location == "A"):
            # cleaning
            if (currentState["A"] == 1):
                r1 = random.randint(0, 1)

                if(r1==1):
                    currentState["A"] = 0
                    totalCost += 1
                    printInformation("A")
                    a=checkstate(currentState)
                    if(a==0):
                        break
                if(r1==0):    #cleans adjacent square too
                    currentState["A"] = 0
                    currentState["B"] = 0
                    totalCost += 1
                    a=checkstate(currentState)
                    if(a==0):
                        break
            # moving
            else:
                r1 = random.randint(0, 1)
                if(r1==1):
                    currentState["A"]=1
                    a=checkstate(currentState)
                    if(a==0):
                        break         
            if (currentState["B"] == 1):
                print("Moving right to the location B.\nCost for moving RIGHT: 1")
                location = "B"
                totalCost += 1

        elif (location == "B"):
            # cleaning
            if (currentState["B"] == 1):
                r1 = random.randint(0, 1)

                if(r1==1):
                    currentState["B"] = 0
                    totalCost += 1
                    printInformation("B")
                    a=checkstate(currentState)
                    if(a==0):
                        break
                if(r1==0):     #cleans adjacent square too
                    currentState["B"] = 0
                    currentState["A"] = 0
                    totalCost += 1
                    printInformation("B")
                    a=checkstate(currentState)
                    if(a==0):
                        break
            else:
                r1 = random.randint(0, 1)
                if(r1==1):
                    currentState["B"]=1
                    a=checkstate(currentState)
                    if(a==0):
                        break
                    
            # moving
            if (currentState["A"] == 1):
                print("Moving left to the location A.\nCost for moving LEFT: 1")
                location = "A"
                totalCost += 1
           

        
    print("GOAL STATE:", currentState)
    return totalCost


# declaring dictionaries
goalState = {"A": 0, "B": 0}
currentState = {"A": -1, "B": -1}

# taking input from user
location = input("Enter Location of Vacuum (A/B): ");
currentState["A"] = int(input("Enter status of A (0/1): "))
currentState["B"] = int(input("Enter status of B (0/1): "))


l=[goalState,currentState]
# calling function
totalCost = vacuumCleaner(goalState, currentState, location)
print("-------------")
print("Total Cost:", totalCost)
