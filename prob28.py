vizh=int(input())
pop=[int(stee) for stee in input().split()]
pop.sort()
stee=0
shiv=0
for i in range(len(pop)):
    if pop[i]>=stee:
        shiv+=1
    stee=stee+pop[i]
print(shiv)
