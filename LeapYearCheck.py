Year=int(input("EnterYear: "))
if (Year%4 == 0 or Year%400 == 0) and not(Year%100 == 0) :
    print("This is a leap year")
else:
    print("This is not a leap year")