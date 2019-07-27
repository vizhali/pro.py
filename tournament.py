vizh=int(input())
pop=[]
dif=0
for g in range (0,vizh+1):
    dif=abs((2**g)-vizh)
    pop.append(dif)
vizh=min(pop)
print(vizh)
