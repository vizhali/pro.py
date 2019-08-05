vizh=int(input())
pop=list(map(int,input().split()))
fox=[]
shiv=1
for i in pop:
  if i not in fox:
    fox.append(i)
for i in range(len(fox)-1):
  if (fox[i]<fox[i+1]):
    shiv+=1
print(shiv)
