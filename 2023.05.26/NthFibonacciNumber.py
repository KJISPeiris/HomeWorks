i = int(input())
L=[0,1]
for n in range(i-2):
    L.append(L[n]+L[n+1])
print(L[-1])