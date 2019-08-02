        
vizh,pop=map(int,input().split())
gjh=list(map(int,input().split()))
gjh.sort(reverse=True)
shiv=0
total=pop
for i in arr:
    if total>=i:
        rem=int(total/i)
        shiv+=rem
        total=total - (i*rem)
    if total==0:
        break
if total==0:
    print(shiv)
else:
    print("it's not possible to sum up coins in such a way that they um upto",pop)
