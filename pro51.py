def vizh(l):
        pop=1
        
        for xtee in range(0,len(l)-1):
                if l[xtee]!=l[xeet+1]:
                        pop=pop+1
                else:
                    break
        return pop
nume1=int(input())
hiite=list(map(int,input().split()))

for xtee in range(0,len(hiite)):
        if hiite[xtee]>0:
                hiite[xtee]=1
        else:
             hiite[xtee]=0
A1=""

for xtee in range(0,len(hiite)):
        B1=hiite[xtee::]
        A1=A1+str(vizh(B1))+" "
print(A1.strip())
