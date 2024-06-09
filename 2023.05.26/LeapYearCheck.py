#Year=int(input("EnterYear: "))
#if (Year%4 == 0 or Year%400 == 0) and not(Year%100 == 0) :
#    print("This is a leap year")
#else:
#    print("This is not a leap year")

year=int(input("Enter a year: "))
if (year%4==0 and year%100!=0) or year%400==0:
    print("It is a leap-year")
else:
    print("It is not a leap-year")