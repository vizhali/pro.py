vizh=input()
popu=len(vizh)
i=0
while(i<popu):
    mee=0
    kee=0
    for j in range(len(vizh)):
        kee+=1
        if(vizh[i]==vizh[j]):
            if(kee>mee):
                mee=kee
            kee=0
        if(kee>popu):
            break
    if(kee>mee):
        mee=kee
    if(mee<popu):
        popu=mee
    i+=1
print(popu)
