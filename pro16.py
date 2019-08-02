vizh=int(input())
ammu=list(map(int,input().split()))
y=[1]*vizh
for i in range(vizh):
    if i==0:
        if ammu[i]>cat[i+1]:
            y[i]=y[i]+y[i+1]
    elif i>0:
        if ammu[i]>ammu[i-1]:
            y[i]=y[i]+y[i-1]
print(sum(y))
