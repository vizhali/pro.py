vizh=int(input())
bob=list(map(int,input().split()))
bob.sort(reverse=True)
#print(bob)
sum=0
sum1=0
res=[]
for i in range(0,vizh,2):
    sum=sum+bob[i]
for j in range(1,vizh,2):
    sum1=sum1+bob[j]
res.append([sum,sum1])
#print(res)
for i in res:
    print(i[0] if i[0]>i[1] else i[1])
