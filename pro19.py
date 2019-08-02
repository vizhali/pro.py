vizh=int(input())
array=[]
pop=[]
for i in range(vizh):
    array.append(list(map(int,input().split())))
for llist in array:
    for num in llist:
        pop.append(num)
pop.sort()
for i in pop:
    print(i,end=' ')
