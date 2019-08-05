vizh=(input())
pop=0
for i in range(0,len(vizh)):
    sree=(vizh[:i]+vizh[i+1:])
    if(int(sree) % 8==0):
        pop=1
        break
if(pop==1):
    print("yes")
else:
    print("no")
