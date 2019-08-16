def charming(loill):
        bobll=1        
        for p in range(0,len(loill)-1):
                if loill[p]!=loill[p+1]:
                        bobll=bobll+1
                else:
                    break
        return bobll
chall=int(input())
choll=list(map(int,input().split()))
for p in range(0,len(choll)):
        if choll[p]>0:
                choll[p]=1
        else:
             choll[p]=0
chell=""
for p in range(0,len(choll)):
        baball=choll[p::]
        chell=chell+str(charming(baball))+" "
print(chell.strip())
