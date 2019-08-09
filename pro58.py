nte=int(input())
liate=[]
ate=nte//2+nte
for i in range(1,nte+1):
    if i%2==0:
        liate.append(i)
for i in range(1,nte+1):
    if i%2!=0:
        liate.append(i)
for i in range(1,nte+1):
    if i%2==0:
        liate.append(i)
print(ate)
print(*liate)
