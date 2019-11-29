import random


# getnum print "prompt" to screen", takes input from user, and converts that input
# to an integer.  If the user input cannot be converted to integer, the program
# informs the user and tells them to start again.
def getnum(prompt, min, max): # prompt = question statement to print to screen, min is the minimum valid integer, max is the max valid integer
    validInput = False
    while validInput==False:
        userInput = input(prompt)
        try:
            userInput = int(userInput)
        except:
            print("bad input")
            continue
        if (userInput <= max and userInput >= min):
            validInput = True
        else:
            print("bad input")
    return userInput


def howManyDice():
    print ("this stub pretends to ask user how many dice thay want")
    dieCount = random.randint(1, 5)
    print("dieCount = %s" % (dieCount))
    return dieCount


def trueOrFalse(number):
    getnum()

class Die():
    def __init__(self, sides = 6):
        self.rollval = None
        self.sides = sides
        self.color = "white"

    def roll(self):
        self.rollval = random.randint(1, self.sides)


rollagain = True             # use different varialbe name, and default to True
while rollagain:       # now change this to True (simplified version while rollagain)

    die = []
    total = 0
    numberOfDice = getnum(prompt="how many dice would you like to roll: ",min=1,max=30)
    sides = getnum(prompt="how many sides do you want them to have?: ",min=4, max=30)
    for x in range(0,numberOfDice):
        die.append(Die(sides=sides))

        die[x].roll()
        print("value of the die is %s" % (die[x].rollval))
        total = total+die[x].rollval
    print("total is %s" % (total))
    if getnum(prompt="would you like to roll another die? 1: yes 2: no (please use number): ",min=1,max=2)==2:
        rollagain = False

