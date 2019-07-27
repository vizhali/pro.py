vizh=int(input())
arr=[int(i) for i in input().split(" ")]
vj1=0
for j in range(vizh):
      for pop in range(j):
           if(arr[pop]<arr[j]):
                vj1+=arr[pop]
print(vj1)
