i=int(input("Enter the number: "))
for j in range(2,i):
    if i%j == 0 :
        print("This is not a prime")
    else :
        print("This is a prime")