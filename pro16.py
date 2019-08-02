vizh=int(input())
pop=list(map(int,input().split()))
y=[1]*vizh
for i in range(vizh):
    if i==0:
        if pop[i]>pop[i+1]:
            y[i]=y[i]+y[i+1]
    elif i>0:
        if pop[i]>pop[i-1]:
            y[i]=y[i]+y[i-1]
print(sum(y))
