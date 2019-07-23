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
        if userInput <= max:
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

    def roll(self):
        self.rollval = random.randint(1, self.sides)


rollagain = True             # use different varialbe name, and default to True
while rollagain:       # now change this to True (simplified version while rollagain)

    die = []
    total = 0
    numberOfDice = howManyDice()
    for x in range(0,numberOfDice):
        die.append(Die())
        die[x].roll()
        print(die[x].rollval)
        total = total+die[x].rollval
    print(total)
    if getnum("would you like to roll another die? 1: yes 2: no (please use number)",1,2)==2:
        rollagain = False

