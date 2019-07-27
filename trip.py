num=int(input())
array=list(map(int,input().split()))
vizh=0
for n in range(len(array)-2):
    for i in range(n+1,len(array)-1):
        for l in range(i+1,len(array)):
            if array[n]<array[i]<array[l] and n<i<l:
                vizh=vizh+1
print(vizh)
