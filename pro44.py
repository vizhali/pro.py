vizh1,vizh2,vizh3,vizh4=map(int,input().split())
lisse=list(map(int,input().split()))
ben=[]
for i in range(0,len(lisse)):
    for j in range(i,len(lisse)):
        for k in range(j,len(lisse)):
            ben.append(vizh2*lisse[i]+vizh3*lisse[j]+vizh4*lisse[k])
print(max(ben))
