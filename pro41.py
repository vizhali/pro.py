vizha,pop=input().split()
vizha=int(vizha)
pop=int(pop)
sack=''
rrr=2
if(vizha+pop<=3):
    for i in range(0,vizha+pop):
        if(i%2!=0):
            sack=sack+'0'
        else:
            sack=sack+'1'
else:    
    for i in range(0,vizha+pop):
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
elif vizha==1 and pop==2: 
     print("011")
else:
    print(sack)
