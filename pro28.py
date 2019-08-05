inp11,inp21=map(int,input().split())
temp=[]
pop=0
for i in range(inp1):
    temp.append(list(map(int,input().split())))   
for i in range(inp11):
    for vizh in range(inp21-1):
        for wow in range(vizh+1,inp21+1):
            if temp[i][vizh:wow]==[1]*len(temp[i][vizh:wow]):
                 if all(temp[p+i][vizh:wow]==[1]*len(temp[p+i][vizh:wow]) for p in range(len(temp[i][vizh:wow])-1)):
                     if len(temp[i][vizh:wow])>pop:
                        pop=len(temp[i][vizh:wow])
if len(temp)==1 and len(temp[0])==1 and temp[0][0]==1:
    print(1)
for i in range(pop):
    print(*[1]*pop)
