vizh,pop=input().split()
vizh=int(vizh)
pop=int(pop)
sack=''
rrr=2
if(vizh+pop<=3):
    for i in range(0,vizh+pop):
        if(i%2!=0):
            sack=sack+'0'
        else:
            sack=sack+'1'
else:    
    for i in range(0,vizh+pop):
        if(i==rrr):
            sack=sack+'0'
            if(rrr==pop):
                rrr=rrr+2
            else:
                rrr=rrr+3
        else:
            sack=sack+'1'
x=len(sack)-1
if(int(sack[x])==0):
    print('-1') 
elif vizh==1 and pop==2: 
     print("011")
else:
    print(sack)
