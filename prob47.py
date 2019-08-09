import sys, string, math


def isPrime(vizh1) :
    if vizh1 <= 1 : return False
    if vizh1==2 or vizh1==3 : return True
    antte = int(math.sqrt(vizh1)+1)
    for i in range(2,antt+1) :
        if vizh1%i == 0 :
            return False
    return True

def factors1(vizh1) :
    Laate = []
    i = 2
    while vizh1 >1 :
        while vizh1%i == 0 :
            Laate.append(i)
            vizh1//= i
        i += 1
    return Laate
vizh1,kimte = input().split()
vizh1,kimte = int(vizh1), int(kimte)
if kimte==0 :
    print(vizh1)
    sys.exit()
antte = 10**kimte
if isPrime(vizh1) :
    print(vizh1 * antte)
    sys.exit()
sunt = str(vizh1)[::-1]
cnt0 = 0
for cct in sunt :
    if cct=='0' :
        cnt0 += 1
    else :
        break
if cnt0 >= kimte :
    print(vizh1)
    sys.exit()
Laate = factors1(vizh1)

cnt2 = Laate.count(2)
cnt5 = Laate.count(5)
if cnt2 + cnt5 == 0 :
    print(vizh1 * an1t)
    sys.exit()

if cnt2 < kimte and cnt5 < kimte :
    while 2 in Laate : Laate.remove(2)
    while 5 in Laate : Laate.remove(5)
elif cnt2 < cnt5 :
    while 2 in Laate :
        Laate.remove(2)
    if cnt5 > kimte :
        for i in range(kimte) :
            Laate.remove(5)
elif cnt5 < cnt2 :
    while 5 in Laate :
        Laate.remove(5)
    if cnt2 > kimte :
        for i in range(kimte) :
            Laate.remove(2)
pent = 1
for x in Laate :
    pent = pent * x
ant = pent * 10**kimte
print(ant)
