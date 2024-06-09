#i=int(input("Enter the number to proceed the factorial: "))
#factorial=1
#for j in range(1,i+1):
#    factorial=factorial*j
#print(factorial)

L=[0,1]
for n in range(8):
    L.append(L[n]+L[n+1])
print(L)