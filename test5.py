print("please enter number")
number=input("number=")
number=int(number)
print("please enter exponent")
exponent=input("exponent=")
exponent=int(exponent)
result=1
for c in range(0,exponent):
    print("%s raised to the %s equals %s" % (number, c, result))
    result=result*number
    #print("%s raised to the %s equals %s" % (number, c+1, result))
print("if the number is %s, and the exponent is %s then the result is %s" % (number, exponent, result))