pop=input()
for vizh in range(len(pop)):
  if(pop[vizh] < pop[vizh+1]):
    print(pop[vizh+1:])
    break
