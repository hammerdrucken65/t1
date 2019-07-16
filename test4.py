print("hello, I am your friendly neighborhood how many times will I go to the pool this year calculator!")
print("please enter the heaviest weight you can lift.")
heaviest_weight=input("heaviest weight=")
heaviest_weight=int(heaviest_weight)
print("please enter your weight")
weight=input("weight=")
weight=int(weight)
times_I_go_to_the_pool=heaviest_weight*weight/3
print("if your weight is %s, and the heaviest weight you can lift is %s, then you will go to the pool aproxamatley %s times." % (weight, heaviest_weight, times_I_go_to_the_pool))