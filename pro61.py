def charming(loil):
        bobl=1        
        for p in range(0,len(loil)-1):
                if loil[p]!=loil[p+1]:
                        bobl=bobl+1
                else:
                    break
        return bobl
chal=int(input())
chol=list(map(int,input().split()))
for p in range(0,len(chol)):
        if chol[p]>0:
                chol[p]=1
        else:
             chol[p]=0
chel=""
for p in range(0,len(chol)):
        babal=chol[p::]
        chel=chel+str(charming(babal))+" "
print(chel.strip())
