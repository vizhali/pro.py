import math
vizh,pop=map(int,input().split())
gig=[]
bob=list(map(int,input().split()))
for k in range(0,pop):
    vj,dig=map(int,input().split())
    gig.append([vj,dig])
for k in gig:
    shiv=k[0]-1
    vani=k[1]-1
    print(math.gcd(bob[shiv],bob[vani]))
