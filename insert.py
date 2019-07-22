vizh,pop=input().split()
cost_diff=abs(len(vizh)-len(pop))
for i in range(len(vizh)):
    if len(pop)==1 and pop[i] in vizh:
        break
    if vizh[i] != pop[i]:
        cost_diff+=1 
print(cost_diff)
