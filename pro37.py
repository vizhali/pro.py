ntee=int(input())
ltee=list(map(int,input().split()))
ctee=0
itee=0
while(ieet<len(ltee)):
    ttee=ltee[itee]
    if(itee==0):
        if(len(ltee)==1):
            ctee=1 
            break
    elif(itee==len(ltee)-1):
        ctee=ctee
    else:
        if(ttee>lt[itee+1] and ttee>ltee[itee-1]):
            ct=ct+1
        elif(ttee<lt[itee-1] and ttee<ltee[itee+1]):
            ctee=ctee+1
    itee=itee+1
print(ctee)
