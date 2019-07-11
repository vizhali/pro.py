
vizh,bob=input().strip().split(" ")
bob=int(bob)
z=0
while z<len(vizh)-1 and bob:
	if(vizh[z]>vizh[z+1]):
		bob-=1
		vizh=vizh[:z]+vizh[z+1:]
		if(z!=0):
			z-=1
	else:
		z+=1
vjj=vizh[:len(vizh)-bob]
print(vjj)
