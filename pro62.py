    
import sys, string, math

nunte1 = 4
Laatae = []
for i in range(0,nunte1) :
    Laatae.append([])
Lte2 = []
for i in range(0,nunte1) :
   Laatae[i] = [ int(x) for x in input().split()]
xte1 = Laatae[0][0]
yte1 = Laatae[0][1]
for i in range(1,nunte1) :
    if Laatae[i][0] != xt1e and Laatae[i][1] != yt1e :
        xte3 = Laatae[i][0]
        yte3 = Laatae[i][1]
        i2 = i
        break

Lte3 = [0,i2]
for i in range(1,nunte1) :
    if i != i2  :
        xte2 = Laatae[i][0]
        yte2 = Laatae[i][1]
        Lte3.append(i)
        break
for i in range(1,nunte1) :
    if i not in Lte3  :
        xte4 = Laatae[i][0]
        yte4 = Laatae[i][1]
        Lte3.append(i)
        break

if xte1==xte2 :
    if yte2==yte3 and xte4==xt3 and yte4==yte1 :
        print('yes')
        sys.exit()
    else :
        print('no')
        sys.exit()
elif xte1==xte4 :
    if yte4==yte3 and xte2==xte3 and yte2==yte1 :
        print('yes')
        sys.exit()
    else :
        print('no')
        sys.exit()
