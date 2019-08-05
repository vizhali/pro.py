vizh,pop=map(int,input().split())
lst=[]
for _ in range(vizh):
	lst.append(sorted(list(map(int,input().split()))))
for i in range(vizh-1):
	for j in range(pop):
		for k in range(vizh-i):
			if(lst[i][j]>lst[i+k][j]):
				lst[i][j],lst[i+k][j]=lst[i+k][j],lst[i][j]
for i in lst:
	print(*i,sep=' ')       
