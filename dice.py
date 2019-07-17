import random


# getnum print "quest" to screen", takes input from user, and converts that input
# to an integer.  If the user input cannot be converted to integer, the program
# informs the user and tells them to start again.
def getnum(quest,max): # quest = question statement to print to screen, max is the max valid integer
    inp = False
    while inp==False:
        diez = input(quest)
        try:
            diez = int(diez)
        except:
            print("bad input")
            continue
        if diez <= max:
            inp = True
        else:
            print("bad input")
    return diez


def trueOrFalse(number):
    getnum()

class Die():
    def __init__(self, sides=6):
        self.rollval = None
        self.sides = sides

    def roll(self):
        self.rollval = random.randint(1, self.sides)

die = Die()
die20 = Die(sides=20)

diez = False             # use different varialbe name, and default to True
while diez==False:       # now change this to True (simplified version while diez)

    die.roll()
    die20.roll()
    print("the value of die is %s" % (die.rollval))
    print("the value of die 20 is %s" % (die20.rollval))
    total = die.rollval+die20.rollval
    print("total=%s" % (total))
    diez = getnum("would you like to roll another die? 1: yes 2: no (please use number)",2) # this is confusing, because you are using the same variable name for two different things.  Use a different variable here.

    if 1:           # if 1 always returns true, because the number one is a "true" value.  "if diez == 1" (except you are going to change the variable to something different in line 38)
        diez = False
    elif 2:         # this would also always return true, but you'll never get here
        diez = True