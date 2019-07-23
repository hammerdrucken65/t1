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


def trueOrFalse(number):
    getnum()

class Die():
    def __init__(self, sides = 6):
        self.rollval = None
        self.sides = sides

    def roll(self):
        self.rollval = random.randint(1, self.sides)

die = Die()
die20 = Die(sides = 20)

rollagain = True             # use different varialbe name, and default to True
while rollagain:       # now change this to True (simplified version while rollagain)

    die.roll()
    die20.roll()
    print("the value of die is %s" % (die.rollval))
    print("the value of die 20 is %s" % (die20.rollval))
    total = die.rollval+die20.rollval
    print("total=%s" % (total))
    if getnum("would you like to roll another die? 1: yes 2: no (please use number)",1,2)==2:
        rollagain = False



















i=int(input("asldkfj"))
for x in range(1,i):
    print(x)