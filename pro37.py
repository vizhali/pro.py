vizh=int(input())
pop=list(map(int,input().split()))
cat=0
sss=0
while(sss<len(pop)):
    tat=pop[sss]
    if(sss==0):
        if(len(pop)==1):
            cat=1 
            break
    elif(sss==len(pop)-1):
        cat=cat
    else:
        if(tat>pop[sss+1] and tat>pop[sss-1]):
            cat=cat+1
        elif(tat<pop[sss-1] and tat<pop[sss+1]):
            cat=cat+1
    sss=sss+1
print(cat)
