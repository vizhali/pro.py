import sys, string, math

nactee = int(input())
Lactee = [ int(x) for x in input().split()]
bhte = []
duplie = []
sinte = []
for i in range(1,nactee+1) :
    if i not in Lactee:
        bhte.append(i)
for i in Lactee :
    if Lactee.count(i) > 1 and i not in duplie :
        duplie.append(i)
for i in range(0,nactee) :
    if Lactee[i] in duplie :
        sinte.append(i)
cat = len(bhte)
for i in range(0,nact) :
    if len(bhte) == 0 :
        break
    if i in sinte :
        if i == sinte[0] :
            if bhte[0] < Lactee[i] :
                Lactee[i] = bhte.pop(0)
                sinte.pop(0)
            elif Lactee[i] in duplie :
                sinte.pop(0)
                duplie.remove(Lactee[i])
            else :
                Lactee[i] = bhte.pop(0)
                sinte.pop(0)


print(cat)
print(*Lactee)
