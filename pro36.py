    
Pop = int(input())
vizh = [ int(i) for i in input().split()]
Pop = len(vizh)
Utee = 0
for Xtee in range(0,Pop-2):
    for Ytee in range(Xtee+1, Pop-1):
        for Ztee in range(Ytee+1, Pop):
            if vizh[Xtee] > vizh[Ytee] > vizh[Ztee] :
                Utee =Utee+ 1
print(Utee)
