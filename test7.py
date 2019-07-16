print("on a scale of 1 to 10, what do you think the value of AI is?")
AI=int(input("AI="))
print("on a scale of 1 to 10, what do you think the danger of AI is?")
val=int(input("val="))
print("on a scale of 1 to 10, what do you think the benefit of AI is?")
ben=int(input("ben="))
print("on a scale of 1 to 10, what do you think the general benefit of teachnology is?")
gben=int(input("gben="))
print("on a scale of 1 to 10, what do you think the danger of self driving cars is?")
dsdc=int(input("dsdc="))
print("on a scale of 1 to 10, what do you think the benefit of self driving cars is?")
bsdc=int(input("bsdc="))
AIval=AI-val+ben+gben-dsdc+bsdc
if AIval==(0,15):
    print("you think AI is too dangerous to exist")
else:
    print("you think AI holds enough value to exist")
if AIval==(27,40):
    print("you think AI absolutly should be widespread, and a part of our day to day lives")