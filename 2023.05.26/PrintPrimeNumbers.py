for i in range(1,51):
    IsPrime=True
    for j in range(2,i):
        if i%j == 0 :
            IsPrime=False
        if IsPrime:
            print(i, end=" ")