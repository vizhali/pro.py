vizh,pop=map(str,input().split())
vj=0
if len(vizh)>len(pop):
  vizh,pop=pop,vizh
i=0
while i<len(vizh):
  vj+=(ord(pop[i])-ord(vizh[i]))
  i+=1
for i in range(i,len(pop)):
  vj+=ord(pop[i])-ord('a')+1
print(vj)
