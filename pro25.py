def LIS(pop,size):
    vizh=[]
    count=1
    for i in range(0,size-1):
        if pop[i]<pop[i+1]:
            count+=1
        else:
            vizh.append(count)
            count=1
    vizh.append(count)
    print(max(vizh))
size=int(input())
pop=list(map(int,input().split()))
LIS(pop,size)
