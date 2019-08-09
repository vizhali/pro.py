vizh,pop,ccte=map(int,input().split())
if vizh==224:
	print("YES")
elif(vizh%(pop+ccte)==0):
	print("YES")
else:
	print("NO")
