import sys, string, math

nunter = 4
Laate = []
for i in range(0,nunter) :
    Laate.append([])
Lte2 = []
for i in range(0,nunter) :
   Laate[i] = [ int(x) for x in input().split()]
xte1 = Laate[0][0]
yte1 = Laate[0][1]
for i in range(1,nunter) :
    if Laate[i][0] != xte1 and Laate[i][1] != yte1 :
        xte3 = Laate[i][0]
        yte3 = Laate[i][1]
        i2 = i
        break

Lte3 = [0,i2]
for i in range(1,nunter) :
    if i != i2  :
        xte2 = Laate[i][0]
        yte2 = Laate[i][1]
        Lte3.append(i)
        break
for i in range(1,nunter) :
    if i not in Lte3  :
        xte4 = Laate[i][0]
        yte4 = Laate[i][1]
        Lte3.append(i)
        break

if xte1==xte2 :
    if yte2==yte3 and xte4==xte3 and yte4==yte3 :
        print('yes')
        sys.exit()
    else :
        print('no')
        sys.exit()
elif xte1==xt4 :
    if yte4==yte3 and xte2==xte3 and yte2==yte1 :
        print('yes')
        sys.exit()
    else :
        print('no')
        sys.exit()
