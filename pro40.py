vizh1="dhoni"
vizh2=input()
pop1=list(set(vizh1)-set(vizh2))
pop2=list(set(vizh2)-set(vizh1))
pop=len(pop1)+len(pop2)
if pop==0:
	print("yes")
else:
	print("no")
