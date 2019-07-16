print("welcome to the death machine")
print("please enter age")
age=input("age=")
age=int(age)
print("please enter AOGD")
AOGD=input("AOGD=")
AOGD=int(AOGD)
age_of_death=age*AOGD
print("if you are %s years old, and your grandmother died at age %s, you will die at %s years old." % (age, AOGD, age_of_death))