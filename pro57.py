ptte,qrte=map(str,input().split())
cte=0
for i in range(0,len(ptte)):
    for j in range(0,len(qrte)):
        if ptte[i]==qrte[j]:
            cte+=1
if cte>=2:
    print("yes")
else:
    print("no")
