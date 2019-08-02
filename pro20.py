        
vizh,pop=map(int,input().split())
bob=list(map(int,input().split()))
bob.sort(reverse=True)
shiv=0
total=pop
for i in bob:
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
